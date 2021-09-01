**Example 1: 测试单向认证TID-2**

测试单向认证TID:021000005d244b1719f5af867cd7445c通过

Input: 

```
tccli iottid AuthTestTid --cli-unfold-argument  \
    --Data AZACEAAAXSRLFxn1r4Z810Rc3VriVaOdFd8NH5AgiaiuBwAAtNBk5qWRh7x9CIIaA+KBhMoKsw6qIQp0+poRIucWz3nwKzEPLs2jlZvJlUbbvjmnoxMoCQ6dXamqOUuh2E3QQOsNWS0vtU9LGraTbN2RN75p7MJLHQpAMwvW+vz1XmFG
```

Output: 
```
{
    "Response": {
        "RequestId": "b410542c-b7b1-439f-99b7-6767cbf41f59",
        "Pass": true
    }
}
```

**Example 2: 测试单向认证TID**

测试单向认证TID:021000005d244b1719f5af867cd7445c不通过

Input: 

```
tccli iottid AuthTestTid --cli-unfold-argument  \
    --Data 12ACEAAAXSRLFxn1r4Z810Rc3VriVaOdFd8NH5AgiaiuBwAAtNBk5qWRh7x9CIIaA+KBhMoKsw6qIQp0+poRIucWz3nwKzEPLs2jlZvJlUbbvjmnoxMoCQ6dXamqOUuh2E3QQOsNWS0vtU9LGraTbN2RN75p7MJLHQpAMwvW+vz1XmFG
```

Output: 
```
{
    "Response": {
        "RequestId": "b410542c-b7b1-439f-99b7-6767cbf41f59",
        "Pass": false
    }
}
```

