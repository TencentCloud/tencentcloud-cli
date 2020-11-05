**Example 1: Deleting an object that is bound to a policy**



Input: 

```
tccli monitor UnBindingPolicyObject --cli-unfold-argument  \
    --Module monitor\
    --GroupId 11111\
    --UniqueId 3dd5113208fd467b2e5d0c1111111111
```

Output: 
```
{
    "Response": {
        "RequestId": "0dbb66c2-1111-1111-1111-11111111111"
    }
}
```

