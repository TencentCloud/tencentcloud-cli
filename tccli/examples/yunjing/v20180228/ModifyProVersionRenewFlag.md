**Example 1: Modifying the renewal flag of CWP Pro**

This example shows you how to modify the renewal flag of CWP Pro.

Input: 

```
tccli yunjing ModifyProVersionRenewFlag --cli-unfold-argument  \
    --RenewFlag NOTIFY_AND_AUTO_RENEW\
    --Quuid add4a78a-0d59-11e8-b7ab-00e081e1a5c5
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

