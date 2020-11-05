**Example 1: Automatically generating redirection relationship**

`lbl-lmeeyb1q` is an HTTPS:443 listener, and `www.abc.com` is a domain name of a forwarding rule under this listener.

Input: 

```
tccli clb AutoRewrite --cli-unfold-argument  \
    --LoadBalancerId lb-r6nx1iby\
    --ListenerId lbl-lmeeyb1q\
    --Domains www.abc.com
```

Output: 
```
{
    "Response": {
        "RequestId": "e351bfdb-147a-4648-b9fe-bbcacff68789"
    }
}
```

