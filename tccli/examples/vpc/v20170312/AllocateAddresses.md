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

