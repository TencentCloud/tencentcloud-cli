**Example 1: 测试示例**

测试开通kerberos

Input: 

```
tccli tchousex CreateKerberos --cli-unfold-argument  \
    --InstanceId instance-kzomgtrd \
    --KerberosConf.Krb5Conf W2xpYmRlZmF1bHRzXQogICAgZG5zX2xvb2t1cF9yZWFsbSA9IGZhbHNlCiAgICBkbnNfbG9va3VwX2tkYyA9IGZhbHNlCiAgICB0aWNrZXRfbGlmZXRpbWUgPSAyNGgKICAgIHJlbmV3X2xpZmV0aW1lID0gN2QKICAgIGZvcndhcmRhYmxlID0gdHJ1ZQogICAgcmRucyA9IGZhbHNlCiAgICBkZWZhdWx0X3JlYWxtID0gRU1SLUM3TU9NR05TCiAgICBkZWZhdWx0X3Rnc19lbmN0eXBlcyA9IGRlczMtY2JjLXNoYTEKICAgIGRlZmF1bHRfdGt0X2VuY3R5cGVzID0gZGVzMy1jYmMtc2hhMQogICAgcGVybWl0dGVkX2VuY3R5cGVzID0gZGVzMy1jYmMtc2hhMQogICAga2RjX3RpbWVvdXQgPSAzMDAwCiAgICBtYXhfcmV0cmllcyA9IDMKICAgIHVkcF9wcmVmZXJlbmNlX2xpbWl0ID0gMQpbcmVhbG1zXQoKICAgICBFTVItQzdNT01HTlMgPSB7CgogICAgICAgIGtkYyA9IDEwLjAuMC45MTo4OAogICAgICAgIGtkYyA9IDEwLjAuMC41ODo4OAogICAgICAgIGFkbWluX3NlcnZlciA9IDEwLjAuMC45MQogICAgICAgIH0KCiAKCltkb21haW5fcmVhbG1dCiMgLmV4YW1wbGUuY29tID0gRVhBTVBMRS5DT00KCgo= \
    --KerberosConf.Principal hadoop/bobpeng@EMR-C7MOMGNS \
    --KerberosConf.Keytab BQIAAABKAAIADEVNUi1DN01PTUdOUwAGaGFkb29wAAdib2JwZW5nAAAAAWkdaIYCABAAGCaYSQJ5vARe2s6/yynEXXqKm4ZeH9olbQAAAAI= \
    --KerberosConf.NameService HDFS190058031 \
    --KerberosConf.NN1Addr 10.0.0.91:4007 \
    --KerberosConf.NN2Addr 10.0.0.58:4007
```

Output: 
```
{
    "Response": {
        "RequestId": "7bfce3bb-86b8-456f-a945-9e849d12f9ed"
    }
}
```

