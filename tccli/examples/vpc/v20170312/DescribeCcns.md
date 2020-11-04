**Example 1: 按ID过滤查询CCN列表**



Input: 

```
tccli vpc DescribeCcns --cli-unfold-argument  \
    --CcnIds ccn-8j0phqix ccn-gree226l
```

Output: 
```
{
    "Response": {
        "CcnSet": [
            {
                "CcnId": "ccn-8j0phqix",
                "CcnName": "test",
                "CcnDescription": "",
                "InstanceCount": 0,
                "CreateTime": "2018-06-10 16:21:35",
                "State": "AVAILABLE"
            },
            {
                "CcnId": "ccn-gree226l",
                "CcnName": "test",
                "CcnDescription": "",
                "InstanceCount": 1,
                "CreateTime": "2018-06-10 22:04:56",
                "State": "ISOLATED"
            }
        ],
        "TotalCount": 2,
        "RequestId": "73159790-39b3-48e8-9d61-29e11eed1acd"
    }
}
```

**Example 2: 按名称过滤查询CCN列表**



Input: 

```
tccli vpc DescribeCcns --cli-unfold-argument  \
    --Filters.0.Name ccn-name\
    --Filters.0.Values test
```

Output: 
```
{
    "Response": {
        "CcnSet": [
            {
                "CcnId": "ccn-8j0phqix",
                "CcnName": "test",
                "CcnDescription": "",
                "InstanceCount": 0,
                "CreateTime": "2018-06-10 16:21:35",
                "State": "AVAILABLE"
            },
            {
                "CcnId": "ccn-gree226l",
                "CcnName": "test",
                "CcnDescription": "",
                "InstanceCount": 1,
                "CreateTime": "2018-06-10 22:04:56",
                "State": "ISOLATED"
            },
            {
                "CcnId": "ccn-nzwnkrgt",
                "CcnName": "test name",
                "CcnDescription": "test description",
                "InstanceCount": 0,
                "CreateTime": "2018-06-18 11:18:30",
                "State": "AVAILABLE"
            },
            {
                "CcnId": "ccn-nrych3fn",
                "CcnName": "test name",
                "CcnDescription": "test description",
                "InstanceCount": 0,
                "CreateTime": "2018-06-18 11:20:58",
                "State": "AVAILABLE"
            }
        ],
        "TotalCount": 4,
        "RequestId": "d1f17eef-c7c9-4abe-b9ea-843fa5c8db16"
    }
}
```

**Example 3: 查询绑定了标签的CCN列表**

查询绑定了标签键值对（env:test）的ccn。

Input: 

```
tccli vpc DescribeCcns --cli-unfold-argument  \
    --Filters.0.Name tag:env\
    --Filters.0.Values test
```

Output: 
```
{
    "Response": {
        "CcnSet": [
            {
                "CcnId": "ccn-nzwnkrgt",
                "CcnName": "test name",
                "CcnDescription": "test description",
                "InstanceCount": 0,
                "CreateTime": "2018-06-18 11:18:30",
                "State": "AVAILABLE",
                "TagSet": [
                    {
                        "Key": "env",
                        "Value": "test"
                    },
                    {
                        "Key": "TAG_TEST",
                        "Value": "1111"
                    }
                ]
            },
            {
                "CcnId": "ccn-nrych3fn",
                "CcnName": "test name",
                "CcnDescription": "test description",
                "InstanceCount": 0,
                "CreateTime": "2018-06-18 11:20:58",
                "State": "AVAILABLE",
                "TagSet": [
                    {
                        "Key": "TAG_TEST1",
                        "Value": "tag1"
                    },
                    {
                        "Key": "env",
                        "Value": "test"
                    }
                ]
            }
        ],
        "TotalCount": 2,
        "RequestId": "d1f17eef-c7c9-4abe-b9ea-843fa5c8db16"
    }
}
```

