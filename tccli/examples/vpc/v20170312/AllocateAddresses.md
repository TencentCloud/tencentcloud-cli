**Example 1: 创建加速IP**

需开通Anycast公网加速白名单

Input: 

```
tccli vpc AllocateAddresses --cli-unfold-argument  \
    --AddressCount 1 \
    --AddressType AnycastEIP
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            "eip-m44ku5d2"
        ],
        "TaskId": "61531428",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

**Example 2: 创建常规IP**

创建常规IP。

Input: 

```
tccli vpc AllocateAddresses --cli-unfold-argument  \
    --AddressCount 1
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            "eip-m44ku5d2"
        ],
        "TaskId": "61531421",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

**Example 3: 创建静态单线IP**

需开通静态单线IP白名单

Input: 

```
tccli vpc AllocateAddresses --cli-unfold-argument  \
    --AddressCount 1 \
    --InternetServiceProvider CTCC
```

Output: 
```
{
    "Response": {
        "AddressSet": [
            "eip-m44ku5d2"
        ],
        "TaskId": "61531429",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

**Example 4: 申请EIP失败**

幂等请求失败，更新幂等参数。

Input: 

```
tccli vpc AllocateAddresses --cli-unfold-argument  \
    --ClientToken b8fcdf80-248a-4095-bfa3-7f59df1aec
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnsupportedOperation.DeliveryFailed",
            "Message": "发货失败，请更新`ClientToken`并重试。"
        },
        "RequestId": "8e176c15-f087-4816-a270-306cf87229a6"
    }
}
```

