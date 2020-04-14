import json
def estimator(data):
    #data_dict = json.loads(data)
		
    reportedCases = data['reportedCases']
    periodType = data['periodType']
    timeToElapse = data['timeToElapse']
    totalHospitalBeds = data['totalHospitalBeds']
    avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']
    factor = 1
    days = 1
	
    if periodType == 'months':
        factor = (timeToElapse * 30) // 3
        days = timeToElapse * 30
    elif periodType == 'weeks':
        factor = (timeToElapse * 7) // 3
        days = timeToElapse * 7
    else:
        factor = timeToElapse // 3 
        days = timeToElapse

    impact = {'currentlyInfected': reportedCases * 10, 
	      'infectionsByRequestedTime': (reportedCases * 10 * (2 ** factor)),
	      'severeCasesByRequestedTime': int(0.15 * (reportedCases * 10 * (2 ** factor))),
	      'hospitalBedsByRequestedTime': int((0.35 * totalHospitalBeds) - (0.15 * (reportedCases * 10 * (2 ** factor)))),
	      'casesForICUByRequestedTime': int(0.05 * (reportedCases * 10 * (2 ** factor))),
	      'casesForVentilatorsByRequestedTime': int(0.02 * (reportedCases * 10 * (2 ** factor))),
	      'dollarsInFlight': (avgDailyIncomeInUSD * avgDailyIncomePopulation * days * (reportedCases * 10 * (2 ** factor))) // days }

    severeImpact = {'currentlyInfected': reportedCases * 50,
		    'infectionsByRequestedTime': (reportedCases * 50 * (2 ** factor)), 
		    'severeCasesByRequestedTime': int(0.15 * (reportedCases * 50 * (2 ** factor))), 
		    'hospitalBedsByRequestedTime': int((0.35 * totalHospitalBeds) - (0.15 * (reportedCases * 50 * (2 ** factor)))), 
		    'casesForICUByRequestedTime': int(0.05 * (reportedCases * 50 * (2 ** factor))),
		    'casesForVentilatorsByRequestedTime': int(0.02 * (reportedCases * 50 * (2 ** factor))),
		    'dollarsInFlight': (avgDailyIncomeInUSD * avgDailyIncomePopulation * (reportedCases * 50 * (2 ** factor))) // days}

    #estimate = {'impact': impact, 'severeImpact': severeImpact}
    output = {'data': data, 'impact': impact, 'severeImpact': severeImpact}

    return (output)
