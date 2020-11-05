**Example 1: Modifying the Forwarding Rule Domain Name of a Layer-7 Listener**

Modify the forwarding rule domain name of a layer-7 listener.

Input: 

```
tccli gaap ModifyDomain --cli-unfold-argument  \
    --ListenerId 0\
    --OldDomain a.a.com\
    --NewDomain b.b.com\
    --CertificateId default
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

