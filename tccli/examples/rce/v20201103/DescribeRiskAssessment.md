**Example 1: DescribeRiskAssessment**



Input: 

```
tccli rce DescribeRiskAssessment --cli-unfold-argument  \
    --BizCryptoData.IsAuthorized 1 \
    --BizCryptoData.CryptoType 1 \
    --BizCryptoData.CryptoContent tLMs/D/1SHZD/DfNsGCu48LXgeMICppNIWrsdr1jdbzIX+zI3e+FdK8RXzDDtLRIlFq/95qMh1Fh2P80PE8iRbIt+t6L0b4Up8FDzmPwKkMXsYCFAVbpoHG+p9wFSNfJ4Q94dpsD2BCk5yul9ihwoHfSbJJdCgiwVZOO/3OFPfrYsLXQToZezvj1+HhhxXGXtYgPPp60gXHg3gon1BWVeHf0bRrhyGyCYoM4VZa5K2nwvHC7noSWUEHjDHR+TDId/kHMnKN7avjX+8g7XqKz0QIFEkr9OeuegOjxWmKj/TzuTZJ9coqJJbjLOC6KjB8KOnFYNobC5HKpUzO/9dveevU42jNXAugMSUwsOYAuEpUyf/HNJWJ8EKgxzNnE0Nz2KnEiTXS/ha0y6Ir6hSglgHTxv5rShQdqYvnoXVwlExyWaJhX21nOB66G3LwDpfrLJRxbnwJj4avqAkvdfVe+DCNPSAQ3HBVVaExaTnHHwbjdA2BJ6QeHXgtObp9K/2RarEtBB3xSjLLo/5ENW8oBZ/5IDgBU05Nq5P9Y7oWkNmzhI7IsOLZ4VKQL7iifnPvH+FnNdnoeq+LTwAFosv8j7OoqdlZRQk8mmQJTUiY3xLw=
```

Output: 
```
{
    "Response": {
        "Data": {
            "UUid": "c9fca58f-de00-44b8-8c42-50b91a092f9c",
            "Code": 0,
            "Message": "OK",
            "Value": {
                "RiskLevel": "pass",
                "RiskType": [
                    1,
                    101,
                    201,
                    2012
                ]
            }
        },
        "RequestId": "a6227506-5f00-43cf-9a4c-66fe931cefc9"
    }
}
```

