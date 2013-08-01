
people = "Pete	Sean	Laura	Haley	Emalyn	Margo	Evan".split('\t')

bidsStr = """310	340	320	315	320	300	305
310	340	320	335	320	300	305
310	375	310	335	310	365	315
310	375	310	335	310	345	315
305	325	290	300	290	300	335
305	325	285	315	285	300	300
250	20	265	165	265	190	225"""

bids = map(
	lambda l: map(lambda i: int(i), l.split('\t')), 
	bidsStr.split('\n')
)

import copy

def findUsed(bids, curPersonIdx, remainingRoomIndices, assignmentsSoFar, sumSoFar):
	if curPersonIdx == len(bids):
		return sumSoFar, assignmentsSoFar

	maxSum = -1
	bestAssignment = {}
	for i in remainingRoomIndices:
		curBid = bids[i][curPersonIdx]
		assignmentsSoFar[people[curPersonIdx]] = {"room": i, "price": curBid}
		curSum, curAssignment = findUsed(bids, curPersonIdx + 1, remainingRoomIndices - set([i]), assignmentsSoFar, sumSoFar + curBid)
		if curSum > maxSum:
			maxSum = curSum
			bestAssignment = copy.copy(curAssignment)

	return maxSum, bestAssignment

bestSum, bestAssignment = findUsed(bids, 0, set(range(len(bids))), {}, 0)

actualRent = 2100
surplus = (bestSum - actualRent)*1.0/len(people)

print 'Found sum of %d with surplus of %f per person' % (bestSum, surplus)
print ''

for name in people:
	v = bestAssignment[name]
	print '\t%s' % name
	print '\t\troom: %d' % (v['room'] + 1)
	print '\t\tbid price: %d' % (v['price'])
	print '\t\treduced price: %f' % (v['price'] - surplus)
	print ''
