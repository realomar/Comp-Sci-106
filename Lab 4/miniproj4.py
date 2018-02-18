from statistics import *
import math

def percentile(x, s_mean, s_stdev):
    """ Computes the percentile of data value x within a data set
    whose mean and standard deviation are s_mean and s_stdev. This assumes
    a normal distribution and uses the cumulative distribution function, phi(o)
    """
    o = (x - s_mean) / s_stdev
    return (1.0 + math.erf(o / math.sqrt(2.0))) / 2.0



#----------- PASTE YOUR FUNCTIONS FOR PARTS 1, 2, and 3 HERE -------------------








    


#-------------------- PROVIDED CODE ---------------------------

#----------- Uses PART 1 code to parse data sets ------------------
# Original source data from:
#https://wwwn.cdc.gov/nchs/nhanes/search/nnyfsdata.aspx?Component=Examination
#https://wwwn.cdc.gov/nchs/nhanes/search/nnyfsdata.aspx?Component=Questionnaire

def choose_max_key(d, keys):
    m = {}
    for (k,v) in d.items():
        v = choose_max(v, keys)
        if v:
            m[k] = v
    return m

d_upper = choose_max_key(parse('Y_MPX.csv'), ['MPXPULL'])
d_core = choose_max_key(parse('Y_PLX.csv'), ['MPXPLANK'])
d_lower = choose_max_key(parse('Y_LMX.csv'), ['LBLEXT1','LBLEXT2','LBLEXT3','LBREXT1','LBREXT2','LBREXT3'])
d_endurance = choose_max_key(parse('Y_CEX.csv'), ['CEDEXLEN'])
d_height = choose_max_key(parse('Y_BMX.csv'), ['BMXHT'])
d_list = [d_height, d_upper, d_core, d_lower, d_endurance]

# meta data from NHANES about what sport activites PAQ724 column codes indicate
sport_mapping = {'Y': 'track & field', 'P': 'martial arts', 'S': 'running', 'AD': 'backyard games', 'A': 'aerobics', 'AF': 'horseback riding', 'CM': 'other', 'J': 'gymnastics', 'AB': 'wrestling', 'E': 'cheerleading', 'W': 'swimming', 'D': 'bike riding', 'F': 'dance', 'G': 'field hockey', 'C': 'basketball', 'U': 'skateboarding', 'AA': 'walking', 'I': 'golf', 'AE': 'trampoline', 'Z': 'volleyball', 'B': 'baseball', 'O': 'lacrosse', 'V': 'soccer', 'M': 'ice skating', 'Q': 'playing games', 'R': 'roller blading', 'X': 'tennis', 'K': 'hiking', 'N': 'jumping rope', 'L': 'ice hockey', 'T': 'scooter riding', 'H': 'football', 'AC': 'frisbee'}


#----------- Uses PART 2 code to build a model ------------------

def key_startswith(d, key_start):
    result = []
    for (k, v) in d.items():
        if k.startswith(key_start) and not 'nan' in v:
            result.append(k[len(key_start):])
    return result

def summary_keys(d, key_start):
    result = {}
    for (i, p) in d.items():
        matches = key_startswith(p, key_start)
        if matches:
            result[i] = matches
    return result

stats = [(mean(d.values()), stdev(d.values())) for d in d_list]
d_all = merge(d_list)

model = {k:percentile_list(v,stats) for (k,v) in d_all.items()}
model_predictions = summary_keys(parse('Y_PAQ.csv'), 'PAQ724')

#----------- Uses PART 3 code to make a recommendation ------------------

def weighted_knn_recommendation(model, model_predictions, subject_values, max_weight):
    """
    Uses KNN (K- Nearest Neighbors) approach with Euclidean distance
    See https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
    for more details.
    """
    min_distance = 1 / max_weight
    counts = {}
    sums = {}
    
    # for each known data entry in our model, compute the subject's distance
    #  to the entry and weight the predictions of physical activity accordingly
    for (model_key, model_values) in model.items():
        if model_key in model_predictions:
            d = distance(subject_values, model_values)
            if d < min_distance:
                weight = max_weight
            else:
                weight = 1 / d            
            for s in model_predictions[model_key]:
                counts[s] = counts.get(s,0) + 1
                sums[s] = sums.get(s,0) + weight  
        
    return sorted([(s/counts[k],k) for k,s in sums.items()], reverse=True)

def make_recommendation(subject, values):
    """
    Makes a recommendation for the given subject with data values
    """
    p = percentile_list(values, stats)
    
    topten = weighted_knn_recommendation(model, model_predictions, p, 100)[:10]
    topten_strings = ["{:.2f} {}".format(rating, sport_mapping[code]) 
                      for rating,code in topten]
    return subject +"= " + ", ".join(topten_strings)  



# some sample test subjects to make recommendations for
# format is [height in cm, number of pull ups, leg extension pounds, 
#            plank seconds, treadmill endurance test seconds]
test_subjects = {"George":[130.0, 20.0, 150.0, 85.0, 900.0],
                 "Alice":[135.0, 10.0, 110.0, 25.0, 525.0],
                 "David":[140.0, 10.0, 60.0, 70.0, 750.0],
                 "Olivia":[155.0, 10.0, 125.0, 70.0, 500.0],
                 "Hayden":[160.0, 1.0, 20.0, 25.0, 200.0]}


#-------------------- UNIT TESTS ---------------------------

TEST1 = summary_keys({'1':{'XA':'2', 'XB':'3', 'XC':'nan', 'XD':'nan'},
                      '2':{'A':'2', 'B':'3', 'XC':'8', 'XD':'nan'},
                      '3':{'XA':'nan', 'XB':'nan', 'XC':'nan', 'XD':'nan'}},
                     'X')
assert sorted(TEST1['1']) == ['A', 'B'] and TEST1['2'] == ['C'] and '3' not in TEST1
TEST2 = summary_keys({'QA':{'fooA':'nan', 'fooB':'10'},
                      'QB':{'fooA':'5', 'barB':'10'}},
                     'fo')
assert TEST2['QA'] == ['oB'] and TEST2['QB'] == ['oA']


assert sorted(key_startswith({'XA':'2', 'XB':'3', 'XC':'nan', 'XD':'nan'}, 
                          'X')) == ['A','B']
assert sorted(key_startswith({'XA':'nan', 'XB':'nan'}, 
                      'X')) == []
assert sorted(key_startswith({'fooA':'nan', 'fooB':'10'}, 
                      'fo')) == ['oB']
assert sorted(key_startswith({'fooA':'5', 'barB':'10'}, 
                      'fo')) == ['oA']

D1 = {1:5,2:7}
D2 = {2:3,3:10}
D3 = {2:8,4:1}

assert merge([D1,D2,D3]) == {2:[7, 3, 8]}

assert distance([1, 1, 3], [2, 2, 3]) == 1.4142135623730951
assert distance([1, 2, 3], [2, 2, 3]) == 1.0
assert distance([2, 2, 3], [2, 2, 3]) == 0.0
assert distance([1, 1], [2, 2]) == 1.4142135623730951

if __name__ == "__main__":
    for s, v in test_subjects.items():
        print(make_recommendation(s, v))
