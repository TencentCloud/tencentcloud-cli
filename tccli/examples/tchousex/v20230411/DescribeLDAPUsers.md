**Example 1: ldap用户列表**



Input: 

```
tccli tchousex DescribeLDAPUsers --cli-unfold-argument  \
    --InstanceId instance-6nhjaors \
    --Limit 200 \
    --Offset 0 \
    --UserToken eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6ImUxZTIxMGRmLTA4YTAtNDEwOC04NWMyLTRjNDFjZTE2MDAxMyIsImF1dGhvcml6ZWQiOnRydWUsImNlcnQiOiJ7XCJUbXBTZWNyZXRJZFwiOlwiQUtJRENwVElXNVV0TEhmYmx3ZVRxdVR6YXlUM0VDb3hOSUZNc3JURTFlbkl4b3dyRXhzZjlXQldudnJrZWJpVFBBaHlcIixcIlRtcFNlY3JldEtleVwiOlwiZDNlRkw5MVZudmNGUWpoZXJwTEEweGRkVEJKcEtMbFYxZzVORitCdmtwcz1cIixcIlRva2VuXCI6XCJJbnZUTDEyTUhzT2ZxMkg1MnhQY0RRbVpReXR1UE5EYWQxY2U2ZGU5N2FlMzQ5MWYzNjM2MDBmYTg0MTkxODcxaFk5YUZiOU1ucDZUMFNYZGtnLVVDbEJSNG9KMVJ2Y0pLSkwwSlFoOHozRGthdkFURHoxemxjeENBRVJING9OcmN4U3N5NHFHdFVCNTNmblVzeEEzZGhDM1BQaEdRRVpITDdpOVhyNTlKN2N5SkpacTlkSnh2QWN4ckRSc1F6azNZRzFXTFMxaDZ3SkI4amNrMExoUWY4bEVwLVlGSEJSUF8yekl6Qm5rUHg3VDY5UEZnU1hac0dHWVNzX3phRFR2d25ZNmR5LUpzZjlBeVk0NU1aS0FmLTZxdlNRQ00wLWJURk96dkRHNUo3RHVpQ08wVXNoWTZ3alA1UzhEZ3NXTkxMTHEtaDFBTTV2c2sweWhUc2p0Y3YzMlpBUVhCekV3NElvbnBmcVdhbEN5UEp4REdaM0NaMzlPUVZtYWcyYlQtdVllbTB4QXpsTjJleUc4SkFwcHN3XCJ9IiwiaW5zdGFuY2VfaWQiOiJpbnN0YW5jZS02bmhqYW9ycyIsInVzZXJfbmFtZSI6IjEwMDAwNjA3ODk3NSJ9.hJDFkgWMmZ-R8IcLufA_cA1CL34Qs3CmumgsdCxQ7jQ
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "bc9726a0-7b88-4285-afe1-50ebc6a927e8",
        "ReturnData": "{\"TotalCount\":5,\"LdapUserList\":[{\"Name\":\"hadoop\"},{\"Name\":\"root\"},{\"Name\":\"user01\"},{\"Name\":\"user02\"},{\"Name\":\"user03\"}]}"
    }
}
```

