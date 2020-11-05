**Example 1: Modifying spread placement group attributes**

This example shows you how to modify the attributes of a spread placement group.

Input: 

```
tccli cvm ModifyDisasterRecoverGroupAttribute --cli-unfold-argument  \
    --DisasterRecoverGroupId ps-58l1hu01\
    --Name 'Physical machine disaster recovery group 1'
```

Output: 
```
{
    "Response": {
        "RequestId": "6e185c04-116f-47b7-b21c-e13580c5d0f2"
    }
}
```

