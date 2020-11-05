**Example 1: Creating an Anycast EIP**

This example shows you how to create an Anycast EIP, provided that you are an Anycast Internet Acceleration (AIA) beta user.

Input: 

```
tccli vpc AllocateAddresses --cli-unfold-argument  \
    --AddressCount 1\
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

**Example 2: Creating a regular IP address**



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

**Example 3: Creating a static single-line IP address**

This example shows you how to create a static single-line IP address, provided that you are a static single-line IP beta user.

Input: 

```
tccli vpc AllocateAddresses --cli-unfold-argument  \
    --AddressCount 1\
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

