**Example 1: Deleting a Trigger**

You use this function to delete a trigger.

Input: 

```
tccli scf DeleteTrigger --cli-unfold-argument  \
    --FunctionName ledDummyAPITest\
    --TriggerName test3\
    --Type timer
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

