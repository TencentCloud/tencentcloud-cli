**Example 1: Blacklisting**

This example shows you how to blacklist IPs. You need to specify the header field storing real client IPs to enable the blacklist feature first, and then you can blacklist IPs (you can delete IPs from the blacklist or clear the blacklist in a similar way).

Input: 

```
tccli clb ModifyBlockIPList --cli-unfold-argument  \
    --LoadBalancerIds lb-6efswuxa\
    --Type add_blocked\
    --BlockIPList 1.2.3.4\
    --ExpireTime 3000\
    --AddStrategy fifo\
    --ClientIPField client_ip_test
```

Output: 
```
{
    "Response": {
        "JodId": "localjob010916173469001234567890",
        "RequestId": "83329908-a282-4f9f-82ab-033a3025baff"
    }
}
```

**Example 2: Setting header to enable blacklist feature**

This example shows you how to use the blacklist feature. You need to set the header first by specifying the header field storing real client IPs to enable the blacklist feature.

Input: 

```
tccli clb ModifyBlockIPList --cli-unfold-argument  \
    --LoadBalancerIds lb-6efswuxa\
    --Type add_customized_field\
    --ClientIPField client_ip_test
```

Output: 
```
{
    "Response": {
        "JodId": "localjob010916173469001234512345",
        "RequestId": "83329908-a282-4f9f-82ab-033a30212345"
    }
}
```

