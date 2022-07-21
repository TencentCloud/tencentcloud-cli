**Example 1: demo**



Input: 

```
tccli vpc DescribeEniLimitAllInternal --cli-unfold-argument  \
    --Owner 251197522
```

Output: 
```
{
    "Response": {
        "SubEniLimit": [
            {
                "LowerMem": 1,
                "LowerCpu": 1,
                "Limit": 100
            },
            {
                "LowerMem": 2,
                "LowerCpu": 1,
                "Limit": 100
            },
            {
                "LowerMem": 0,
                "LowerCpu": 2,
                "Limit": 100
            },
            {
                "LowerMem": 0,
                "LowerCpu": 4,
                "Limit": 100
            },
            {
                "LowerMem": 16,
                "LowerCpu": 4,
                "Limit": 100
            },
            {
                "LowerMem": 0,
                "LowerCpu": 8,
                "Limit": 100
            },
            {
                "LowerMem": 0,
                "LowerCpu": 16,
                "Limit": 100
            }
        ],
        "SubEniPipLimit": [
            {
                "LowerMem": 1,
                "LowerCpu": 1,
                "Limit": 8
            },
            {
                "LowerMem": 2,
                "LowerCpu": 1,
                "Limit": 8
            },
            {
                "LowerMem": 0,
                "LowerCpu": 2,
                "Limit": 8
            },
            {
                "LowerMem": 0,
                "LowerCpu": 4,
                "Limit": 8
            },
            {
                "LowerMem": 16,
                "LowerCpu": 4,
                "Limit": 8
            },
            {
                "LowerMem": 0,
                "LowerCpu": 8,
                "Limit": 8
            },
            {
                "LowerMem": 0,
                "LowerCpu": 16,
                "Limit": 8
            }
        ],
        "PipLimitEx": [
            {
                "LowerMem": 1,
                "LowerCpu": 1,
                "Limit": 0
            },
            {
                "LowerMem": 2,
                "LowerCpu": 1,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 2,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 4,
                "Limit": 0
            },
            {
                "LowerMem": 16,
                "LowerCpu": 4,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 8,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 16,
                "Limit": 0
            }
        ],
        "EniLimit": [
            {
                "LowerMem": 1,
                "LowerCpu": 1,
                "Limit": 2
            },
            {
                "LowerMem": 2,
                "LowerCpu": 1,
                "Limit": 2
            },
            {
                "LowerMem": 0,
                "LowerCpu": 2,
                "Limit": 2
            },
            {
                "LowerMem": 0,
                "LowerCpu": 4,
                "Limit": 4
            },
            {
                "LowerMem": 16,
                "LowerCpu": 4,
                "Limit": 4
            },
            {
                "LowerMem": 0,
                "LowerCpu": 8,
                "Limit": 6
            },
            {
                "LowerMem": 0,
                "LowerCpu": 16,
                "Limit": 8
            }
        ],
        "PipLimit": [
            {
                "LowerMem": 1,
                "LowerCpu": 1,
                "Limit": 2
            },
            {
                "LowerMem": 2,
                "LowerCpu": 1,
                "Limit": 6
            },
            {
                "LowerMem": 0,
                "LowerCpu": 2,
                "Limit": 10
            },
            {
                "LowerMem": 0,
                "LowerCpu": 4,
                "Limit": 10
            },
            {
                "LowerMem": 16,
                "LowerCpu": 4,
                "Limit": 20
            },
            {
                "LowerMem": 0,
                "LowerCpu": 8,
                "Limit": 20
            },
            {
                "LowerMem": 0,
                "LowerCpu": 16,
                "Limit": 30
            }
        ],
        "EniLimitEx": [
            {
                "LowerMem": 1,
                "LowerCpu": 1,
                "Limit": 0
            },
            {
                "LowerMem": 2,
                "LowerCpu": 1,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 2,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 4,
                "Limit": 0
            },
            {
                "LowerMem": 16,
                "LowerCpu": 4,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 8,
                "Limit": 0
            },
            {
                "LowerMem": 0,
                "LowerCpu": 16,
                "Limit": 0
            }
        ],
        "RequestId": "64ef9bd5-1824-4733-a19b-603d0fa26843"
    }
}
```

