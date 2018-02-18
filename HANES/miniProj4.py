# Omar Ahmad / Ryan Fisher
# PART 1
def data_dictionary(headers, values):
    '''
    Turns two lists of strings into a dictionary
    Inputs: Two lists of strings, equal length
    Returns: A dictionary with the first list as keys and the second list as respective definitions.
    '''
    dataDict = {}
    inc = 0
    while inc < len(headers):
        dataDict.update({headers[inc]:values[inc]})
        inc += 1
    return dataDict

def choose_max(inputDict, keyList):
    '''
    Finds the maximum value among a given list of keys in a dictionary.
    Inputs: A dictionary and a list of keys
    Returns: A float for the maximum value extracted. None if 'nan' or no relevant values found
    '''
    foundValues = []
    for val in keyList:
      if val in inputDict:
        if inputDict[val] == 'nan':
          return None
        else:
          foundValues.append(float(inputDict[val]))
    return max(foundValues)

def parse(filename):
  '''
  Turns a csv table into a nested dictionary.
  Input: the path of a csv file holding id, age, and name for multiple entries.
  Returns: A nested dictionary with those values
  '''
  csvTable = open(filename, 'r')
  line1 = csvTable.readline().strip().split(',')
  nestDict = {}
  for line in csvTable:
    vals = line.strip().split(',')
    nestDict[vals[0]] = data_dictionary(line1,vals)
  return nestDict

# PART 2
import math
def percentile(x, s_mean, s_stdev):
    """ Computes the percentile of data value x within a data set
    whose mean and standard deviation are s_mean and s_stdev. This assumes
    a normal distribution and uses the cumulative distribution function, phi(o)
    """
    o = (x - s_mean) / s_stdev
    return (1.0 + math.erf(o / math.sqrt(2.0))) / 2.0

def percentile_list(vals, valStats):
  '''
  Converts statistical values into percentiles, given mean and stdev
  Inputs: A list of values in a normal distribution, a list of tuples containing mean and standard deviation for that data set.
  Returns: A list of percentile values for each input element.
  '''
  percentiles = []
  for i in range(len(vals)):
    percentiles.append(percentile(vals[i],valStats[i][0],valStats[i][1]))
  return percentiles

def common_keys(lod):
  '''
  Finds the keys that a list of dictionaries has in common.
  Input: list of dictionaries
  Returns: A list of common keys
  '''
  common = lod[0].keys()
  for i in range(len(lod)):
    common = lod[i].keys() & common
  return common

def merge(lod):
  '''
  Merges a list of dictionary into one dictionary with key-value pairs for all common keys.
  Input: A list of dictionaries
  Returns: A dictionary containing all known definitions for each common key
  '''
  m = {}
  for k in common_keys(lod):
      currentVals = []
      for d in lod:
        currentVals.append(d.get(k))
      m.update({k:currentVals})
  return m

# PART 3
def distance(p,q):
  '''
  Computes the Euclidean distance between two Cartesian points
  Inputs: Two lists of values, representing coordinates
  Returns: The straight line distance between the points
  '''
  squareDist = 0
  for i in range(len(p)):
    squareDist += (p[i] - q[i])**2
  return squareDist**0.5
