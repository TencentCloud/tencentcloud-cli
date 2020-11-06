**Example 1: 获取导入主密钥（CMK）材料的参数**



Input: 

```
tccli kms GetParametersForImport --cli-unfold-argument  \
    --KeyId 1ff78c0d-c54b-11e9-9cc9-5254006d0810 \
    --WrappingAlgorithm RSAES_OAEP_SHA_1 \
    --WrappingKeySpec RSA_2048
```

Output: 
```
{
    "Response": {
        "KeyId": "1ff78c0d-c54b-11e9-9cc9-5254006d0810",
        "ImportToken": "Sy+GF4f+XxUan1sfSBfqWQmyJeVO30wcqLEMoW4REpw3adjEFXyCP2yqzV8xdD5GMY4gIZoDfJ33SnnbxDMRND8lzh4mZjzFNM8PsjhYrgVSxIiJOCHupZvD4QcoGco8",
        "PublicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1IjpYRubNKn97lPU0/eR8UBaV11glfQLNqlub+YspXwBsvVqcnSvu5c8GoLTEYGSTVbvsREDCq6VfFoSeoIqbv8aWukxbPGWgI1nu55ocvWwthzROFA5UPGC8LOuH0ftZ5Z7cIaigEenS3ngfo4MYTJtg6/Bl1jJVWvjnKzgswsZeFclSURedSXUcMxfSI344s6I17DTNAQ/vQqyjFGIyo2+JctaxVlY2XuBZf7tPimNdoxAoJ14QxAl1gQGu959xnRJ4rwZbxsklJnEivQqTBeFIiv3KTzFJS6bkz2eqRJ1p4jTBDWbHEWTVt6tdXPj4+4D21RFGAt3706vf4PIrwIDAQAB",
        "ParametersValidTo": 1566614716,
        "RequestId": "5e137679-519f-409f-9a99-579a034cc320"
    }
}
```

