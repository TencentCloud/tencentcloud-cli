**Example 1: Removing user**

This example shows you how to remove users test1 and test2 from room 1234.

Input: 

```
tccli trtc RemoveUser --cli-unfold-argument  \
    --SdkAppId 1400000001\
    --RoomId 1234\
    --UserIds test1 test2 test3 test4 test5 test6 test7 test8 test9 test10
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

