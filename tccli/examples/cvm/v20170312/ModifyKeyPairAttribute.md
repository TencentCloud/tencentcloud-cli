**Example 1: Modifying key pair name**

This example shows you how to modify the key pair name.

Input: 

```
tccli cvm ModifyKeyPairAttribute --cli-unfold-argument  \
    --KeyId skey-mv9yzyjj\
    --KeyName Tencent
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

**Example 2: Modifying key pair description**

This example shows you how to modify the key pair description.

Input: 

```
tccli cvm ModifyKeyPairAttribute --cli-unfold-argument  \
    --KeyId skey-mv9yzyjj\
    --Description Tencent
```

Output: 
```
{
    "Response": {
        "RequestId": "aea2227b-fbb7-4cc7-bf29-d49b2b6db97c"
    }
}
```

