**Example 1: Querying the execution status of an async IP blocking (blacklisting) task**



Input: 

```
tccli clb DescribeBlockIPTask --cli-unfold-argument  \
    --TaskId localjob010916173469001234567890
```

Output: 
```
{
    "Response": {
        "Status": 6,
        "RequestId": "83329908-a282-4f9f-8ab-033a3025baff"
    }
}
```

