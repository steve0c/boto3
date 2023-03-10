#%%

# =============================================================================
# script for listing lambdas
# =============================================================================

#%%
# import libraries

import boto3

#%%
# prep boto3 for Lambda

client = boto3.client('lambda')

#%%
# get lambda functions

response = client.list_functions()

#%%

functions = response['Functions']

#%%

for function in functions:
    print(function['FunctionName'])