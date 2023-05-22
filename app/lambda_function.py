

def lambda_handler(event, context):
    return _sum(event['a'], event['b'])


def _sum(a,b):
    return a+b