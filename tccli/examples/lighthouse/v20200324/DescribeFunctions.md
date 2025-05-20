**Example 1: 查询所有函数**

查询实例下的所有函数。

Input: 

```
tccli lighthouse DescribeFunctions --cli-unfold-argument  \
    --InstanceId lhins-gtn3ojxp \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "FunctionSet": [
            {
                "CreatedTime": "2023-02-23T08:27:55Z",
                "DeployStatus": "RUNNING",
                "DeployVersion": 1,
                "FunctionDescribe": "描述信息",
                "FunctionEntry": {
                    "HttpMethods": [
                        "ANY"
                    ],
                    "HttpPath": "/path2",
                    "NeedAuthenticate": false
                },
                "FunctionName": "function002",
                "Template": "golang-http",
                "UpdatedTime": "2023-02-23T08:27:55Z"
            },
            {
                "CreatedTime": "2023-02-22T03:34:48Z",
                "DeployStatus": "RUNNING",
                "DeployVersion": 1,
                "FunctionDescribe": "这是一条简单的描述",
                "FunctionEntry": {
                    "HttpMethods": [
                        "DELETE",
                        "GET",
                        "POST"
                    ],
                    "HttpPath": "/python3",
                    "NeedAuthenticate": false
                },
                "FunctionName": "python3",
                "Template": "python3-http",
                "UpdatedTime": "2023-02-22T03:34:48Z"
            },
            {
                "CreatedTime": "2023-02-22T02:26:20Z",
                "DeployStatus": "RUNNING",
                "DeployVersion": 4,
                "FunctionDescribe": "修改后的描述",
                "FunctionEntry": {
                    "HttpMethods": [
                        "ANY"
                    ],
                    "HttpPath": "/update",
                    "NeedAuthenticate": false
                },
                "FunctionName": "function-001",
                "Template": "golang-http",
                "UpdatedTime": "2023-02-23T08:37:55Z"
            }
        ],
        "RequestId": "c678aa31-016c-4bdf-a5bc-c4e5b49c7f59",
        "TotalCount": 3
    }
}
```

**Example 2: 根据函数名查询函数**

查询函数名为function-001的函数。

Input: 

```
tccli lighthouse DescribeFunctions --cli-unfold-argument  \
    --InstanceId lhins-gtn3ojxp \
    --FunctionNames function-001 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "FunctionSet": [
            {
                "CreatedTime": "2023-02-22T02:26:20Z",
                "DeployStatus": "RUNNING",
                "DeployVersion": 4,
                "FunctionDescribe": "修改后的描述",
                "FunctionEntry": {
                    "HttpMethods": [
                        "ANY"
                    ],
                    "HttpPath": "/update",
                    "NeedAuthenticate": false
                },
                "FunctionName": "function-001",
                "Template": "golang-http",
                "UpdatedTime": "2023-02-23T08:37:55Z"
            }
        ],
        "RequestId": "834600ae-4102-4e78-b362-6b7ad58670ea",
        "TotalCount": 1
    }
}
```

**Example 3: 根据filter模糊查询函数**

查询函数名包含function的函数

Input: 

```
tccli lighthouse DescribeFunctions --cli-unfold-argument  \
    --InstanceId lhins-gtn3ojxp \
    --Filters.0.Name vague-function-name \
    --Filters.0.Values function \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "FunctionSet": [
            {
                "CreatedTime": "2023-02-23T08:27:55Z",
                "DeployStatus": "RUNNING",
                "DeployVersion": 1,
                "FunctionDescribe": "描述信息",
                "FunctionEntry": {
                    "HttpMethods": [
                        "ANY"
                    ],
                    "HttpPath": "/path2",
                    "NeedAuthenticate": false
                },
                "FunctionName": "function002",
                "Template": "golang-http",
                "UpdatedTime": "2023-02-23T08:27:55Z"
            },
            {
                "CreatedTime": "2023-02-22T02:26:20Z",
                "DeployStatus": "RUNNING",
                "DeployVersion": 4,
                "FunctionDescribe": "修改后的描述",
                "FunctionEntry": {
                    "HttpMethods": [
                        "ANY"
                    ],
                    "HttpPath": "/update",
                    "NeedAuthenticate": false
                },
                "FunctionName": "function-001",
                "Template": "golang-http",
                "UpdatedTime": "2023-02-23T08:37:55Z"
            }
        ],
        "RequestId": "d82943dc-b190-41e3-a961-d9d7a6403335",
        "TotalCount": 2
    }
}
```

