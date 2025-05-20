**Example 1: 查询实例下所有的函数活动**

查询实例lhins-gtn3ojxp下所有的函数活动。

Input: 

```
tccli lighthouse DescribeFunctionActivities --cli-unfold-argument  \
    --InstanceId lhins-gtn3ojxp \
    --Offset 0 \
    --Limit 20 \
    --CreatedTimeBegin 0 \
    --CreatedTimeEnd 0
```

Output: 
```
{
    "Response": {
        "FunctionActivitySet": [
            {
                "ActivityId": "lhfa-a8diredk",
                "ActivityName": "DeployFunction",
                "ActivityState": "SUCCESS",
                "CreatedTime": "2023-02-23T08:33:17Z",
                "EndTime": "2023-02-23T08:33:18Z",
                "ErrorMessage": "",
                "FunctionNames": [
                    "function-001"
                ]
            },
            {
                "ActivityId": "lhfa-o9i15qeg",
                "ActivityName": "CreateFunctionVersion",
                "ActivityState": "SUCCESS",
                "CreatedTime": "2023-02-23T08:31:42Z",
                "EndTime": "2023-02-23T08:31:43Z",
                "ErrorMessage": "",
                "FunctionNames": [
                    "function-001"
                ]
            },
            {
                "ActivityId": "lhfa-k7q4widg",
                "ActivityName": "CreateFunction",
                "ActivityState": "FAILED",
                "CreatedTime": "2023-02-23T08:27:56Z",
                "EndTime": "2023-02-23T08:27:57Z",
                "ErrorMessage": "SW50ZXJuYWwgRXJyb3Iu",
                "FunctionNames": [
                    "function002"
                ]
            }
        ],
        "RequestId": "a5a61025-c0e7-4716-9102-7821db9e0dfd",
        "TotalCount": 3
    }
}
```

**Example 2: 查询指定时间范围内的函数活动**

查询创建时间在1677120579(2023-02-23 10:49:39)到1677206979(2023-02-24 10:49:39)内的函数活动。

Input: 

```
tccli lighthouse DescribeFunctionActivities --cli-unfold-argument  \
    --InstanceId lhins-gtn3ojxp \
    --Offset 0 \
    --Limit 0 \
    --CreatedTimeBegin 1677120579 \
    --CreatedTimeEnd 1677206979
```

Output: 
```
{
    "Response": {
        "FunctionActivitySet": [
            {
                "ActivityId": "lhfa-qj4yiup4",
                "ActivityName": "CreateFunction",
                "ActivityState": "SUCCESS",
                "CreatedTime": "2023-02-24T02:14:29Z",
                "EndTime": "2023-02-24T02:14:30Z",
                "ErrorMessage": "",
                "FunctionNames": [
                    "action-1"
                ]
            }
        ],
        "RequestId": "a775c6c7-6759-4e5f-b2b0-e0310010ecd3",
        "TotalCount": 1
    }
}
```

**Example 3: 查询实例下所有的CreateFunction和DeployFunction函数活动**

查询实例lhins-gtn3ojxp下所有的的CreateFunction和DeployFunction函数活动信息。

Input: 

```
tccli lighthouse DescribeFunctionActivities --cli-unfold-argument  \
    --InstanceId lhins-gtn3ojxp \
    --Filters.0.Name activity-name \
    --Filters.0.Values DeployFunction CreateFunction \
    --Limit 0 \
    --Offset 20 \
    --CreatedTimeBegin 0 \
    --CreatedTimeEnd 0
```

Output: 
```
{
    "Response": {
        "FunctionActivitySet": [
            {
                "ActivityId": "lhfa-a8diredk",
                "ActivityName": "DeployFunction",
                "ActivityState": "SUCCESS",
                "CreatedTime": "2023-02-23T08:33:17Z",
                "EndTime": "2023-02-23T08:33:18Z",
                "ErrorMessage": "",
                "FunctionNames": [
                    "function-001"
                ]
            },
            {
                "ActivityId": "lhfa-k7q4widg",
                "ActivityName": "CreateFunction",
                "ActivityState": "FAILED",
                "CreatedTime": "2023-02-23T08:27:56Z",
                "EndTime": "2023-02-23T08:27:57Z",
                "ErrorMessage": "SW50ZXJuYWwgRXJyb3Iu",
                "FunctionNames": [
                    "function002"
                ]
            }
        ],
        "RequestId": "a5a61025-c0e7-4716-9102-7821db9e0dfd",
        "TotalCount": 2
    }
}
```

