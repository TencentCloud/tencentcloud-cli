**Example 1: 失败**

失败-不是该账号下的实例

Input: 

```
tccli redis AddLanCheck --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.InstanceNotExists",
            "Message": "record not found"
        },
        "RequestId": "296741e1-1246-4ffd-a8a9-53e443bb6617"
    }
}
```

**Example 2: 成功**

成功

Input: 

```
tccli redis AddLanCheck --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4c254150-2ff7-443c-bdf0-89204903ef46"
    }
}
```

**Example 3: 成功2**

成功2

Input: 

```
tccli redis AddLanCheck --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f606f4b4-ade1-41e2-be7b-5d5e2906be6c"
    }
}
```

**Example 4: 添加cvm失败:列表中任务数量最多只能有20个**

添加cvm失败:列表中任务数量最多只能有20个

Input: 

```
tccli redis AddLanCheck --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.Unknown",
            "Message": "添加cvm失败:列表中任务数量最多只能有20个"
        },
        "RequestId": "38b58a6f-9dac-4249-b564-9b2370bc88c3"
    }
}
```

