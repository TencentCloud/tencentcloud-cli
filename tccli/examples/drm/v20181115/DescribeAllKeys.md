**Example 1: 请求示例**

请求Fairplay方案使用的加密密钥

Input: 

```
tccli drm DescribeAllKeys --cli-unfold-argument  \
    --DrmType FAIRPLAY \
    --PublicKey LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FDcmJBUmhXamRTZjlWTGtpZGZGdHhkbzJjUwpOak9PTExhdjdaRWZZSzJtd2NZQ3BqRmtDaG41bi8xcHM2LzcwZjlBRUs1Mmt5T0lSVTVzR0hqcjZEMEgrUUFzCndJZnBya1NzV0krSS9hTGYrM2l0b0tIb0Y5eWRTMEhneHdEcUM0dWRTRFFzRmxKczFTNHZEdm5WbG1IRGNJSkIKdDBLTzZoSVJ4Z2F3bmVxUHN3SURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo \
    --ContentType LiveVideo
```

Output: 
```
{
    "Response": {
        "Keys": [
            {
                "Track": "VIDEO",
                "KeyId": "0c366a3173584fb693be0218c27d4532",
                "Key": "7CiNq5Q+fYTBAIySw/gglnNNeBmw6uQ76erIvD3IQj0=",
                "Iv": "tHUB8M/yvRcHswxRm74hb/ej+q4amjEg0/m8F82ezbg="
            },
            {
                "Track": "AUDIO",
                "KeyId": "0c366a3173584fb693be0218c27d4532",
                "Key": "7CiNq5Q+fYTBAIySw/gglnNNeBmw6uQ76erIvD3IQj0=",
                "Iv": "tHUB8M/yvRcHswxRm74hb/ej+q4amjEg0/m8F82ezbg="
            }
        ],
        "SessionKey": "l2XuCkQx288LFBlbDeKuQ1tfW5LOC2mbRfcAvhD8byFmIq8sqTQ+KA/UMrJyk1lImqgodiOuv+fmVTNbb06IY9vILtBDaN3Ek5/x2c0HUJ3k+kL4gMxOvKmAe/F0+qr0Kbl9CVx6YRntXWcWqD+IJ18D76+tQD1aBP8tS5pwV6Q=",
        "ContentId": "test",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

