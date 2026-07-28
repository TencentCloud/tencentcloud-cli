**Example 1: 示例**



Input: 

```
tccli mqtt DescribeDeviceCertificateBackupHistory --cli-unfold-argument  \
    --InstanceId mqtt-mzj7aqxk \
    --Destination mqtt-******** \
    --DeviceCertificateSn eef6**5*******************f94d707a59913 \
    --CaSn 1b1e3bf*******************a7e66f05
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CaSn": "1b1e3bf3702110125887a3a721a7e66f05522513",
                "CertificateSource": "JITP",
                "ClientId": "clientsun",
                "DeviceCertificate": "-----BEGIN CERTIFICATE-----\n*******************************************************************************************************************************************************************************************************************************************************************************************************************************GMQswCQYD\nVQQGEwJDTjEXMBUGA1UECAwOc3VuLmppYW4ueGlvbmcxDTALBgNVBAcMBHhpYW4x\nEDAOBgNVBAoMB3RlbmNlbnQxCzAJBgNVBAsMAnR4MQswCQYDVQQDDAJ0eDEjMCEG\nCSqGSIb3DQEJARYUamVoYW5zdW5AdGVuY2VudC5jb20wggEiMA0GCSqGSIb3DQEB\nAQUAA4IBDwAwggEKAoIBAQCry5JrV8CoIP6Jt6fw7ZfIVFdVGcUzorrcx7DXgj/F\nR0pWp4UxR00ZNQ4C24jDitEHbiX3ZoULraxKRnrkx1fJIcs+/vyB85gAlfOa9orz\n6rVHVMGz4dc967GT6LhL3yCbE1d8KRmOOrFqC+ZV/hNreotluJ05pWKwL+3ftuzL\nOi6N6UQ4D5TUR8FNeITo/ArrRtZsySV3kDsmCy+FKbe62yuSvO2WIQ4kGAw4MS6D\nmCYQ8RaxEeEu2TtmFWsLuwZy0mtOlLAZ4iuJg6wJHYmvqkIGJeEjP1U4WPWdmVgK\nLhu0V1YRs0k8r1c3j3SZANp40WusWYhr4l9SVw4yfod1AgMBAAGjQjBAMB0GA1Ud\nDgQWBBTXHECdrJBedaw4unI7JWf/KcmUEjAfBgNVHSMEGDAWgBRGllwHWUUctxz7\n41ejQQGGWBoQ3zANBgkqhkiG9w0BAQsFAAOCAQEAxMRW6AXHrVBW9cKbd7XkcIpx\nvfVOrlnYWRN7enz/SHOkO0T+r0JvzQ0IAUHLfcZc99CjM5GY6PyuQtdorINvbSlg\nC7n/ITry1qhAjwgDKQletcyOWCmALwK4YASZ2gDlJ9uUaLaoj9W0amHx8KjaKwu7\nQFMDd1YzUa2SWkrEuaUli2AkhTzeLMVQlSy+n1gQ0B2R4hDhJis/sCRkfKzUEGID\nuuDs7t/KaH7BQqCv0hjdyKJtttPUVw01gGE08tDOHkOLD0BihQUT95o3ush8i2kE\nTCoA+AK4cYilHmP2hpE4s2CZRzaSLebcLziVWvrTyAUGnKHrrFeSYaRzHOmcvQ==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEvDCCA6SgAwIBAgIUGx4783AhEBJYh6OnIafmbwVSJRMwDQYJKoZIhvcNAQEL\nBQAwgZIxCzAJBgNVBAYTAmNuMQ0wCwYDVQQIDAR4aWFuMQ0wCwYDVQQHDARodXlp\nMREwDwYDVQQKDAhqZWhhbnN1bjEWMBQGA1UECwwNdW5pdCBqZWhhbnN1bjEVMBMG\nA1UEAwwMc3Vuamlhbnhpb25nMSMwIQYJKoZIhvcNAQkBFhRqZWhhbnN1bkB0ZW5j\nZW50LmNvbTAeFw0yNDA1MDYwODM2NDFaFw0zNDA1MDQwODM2NDFaMIGSMQswCQYD\nVQQGEwJjbjENMAsGA1UECAwEeGlhbjENMAsGA1UEBwwEaHV5aTERMA8GA1UECgwI\namVoYW5zdW4xFjAUBgNVBAsMDXVuaXQgamVoYW5zdW4xFTATBgNVBAMMDHN1bmpp\nYW54aW9uZzEjMCEGCSqGSIb3DQEJARYUamVoYW5zdW5AdGVuY2VudC5jb20wggEi\nMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDfgKyMAZsTIibnNGG92MUhzM3F\nZPD+be8x4TF+h5EGODWam8+b7z57amNc7gbelNcL1kAa25Xd39E8xZbhHSMP2vby\ndivs/ZGNJYFlOU1g7IGrDEnPaw402g4S0lMHWwvvtwPJxNa5JP6haI+0N3qC0VfX\n900miu1MGvLQ0XGkEVHy37QZ7t2rtbcokwx9oM/Gf2iz+lodV6m9e4wumsAae2kf\nZNeNyDZ7IhRltfIbExoOu7lUT8FN84iYNXRBFtvVlNwrLXjDkN/Jrg3kI8mPo+24\nmcrx6ToGfk2A6YBQLyVVjfGxeERwnWElQiQ+WHJDrIGpTBXbAjn8h/aiIPjlAgMB\nAAGjggEGMIIBAjAdBgNVHQ4EFgQURpZcB1lFHLcc++NXo0EBhlgaEN8wgdIGA1Ud\nIwSByjCBx4AURpZcB1lFHLcc++NXo0EBhlgaEN+hgZikgZUwgZIxCzAJBgNVBAYT\nAmNuMQ0wCwYDVQQIDAR4aWFuMQ0wCwYDVQQHDARodXlpMREwDwYDVQQKDAhqZWhh\nbnN1bjEWMBQGA1UECwwNdW5pdCBqZWhhbnN1bjEVMBMGA1UEAwwMc3Vuamlhbnhp\nb25nMSMwIQYJKoZIhvcNAQkBFhRqZWhhbnN1bkB0ZW5jZW50LmNvbYIUGx4783Ah\nEBJYh6OnIafmbwVSJRMwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEA\nYOfLKq2uSONvUGmGt/EoppiKQeksu+t5MGhSwgL5/74WoQlCF9wSKbvgyhW55iQK\n58dJdg9E18rv9OBURWY3xIdope0ZizmULSEuah6dFYsrcY95mNBHkZ0yK6HtWgRP\nOb8+l1aKJK6cC8BvlHziblAC6bOK+HdpEI+mfVCpxU5B2rhUQEVFH5ogVtE+E9OP\nqamwZlHGDSZvwukBsPkg5EiqP9Sixx102B7uAwym0gXtvrfSKj+KC/mlBkpuKHg8\nfG2aZinrh8RqbUvzpqkVyFfGH2SaJPUchNNA0hdfNKtGfJ5S/BWsSPky82xn+9kp\nfB9p/BeTDdveeb1ATq5ZWw==\n-----END CERTIFICATE-----\n",
                "DeviceCertificateCn": "tx",
                "DeviceCertificateSn": "eef68a582b94254296e54ce754f94d707a59913",
                "Format": "PEM",
                "LastActivationTime": 1765434993699,
                "LastInactivationTime": 0,
                "ModificationTime": 1765439638543,
                "NotAfterTime": 1766155706000,
                "NotBeforeTime": 1734619706000,
                "OrganizationalUnit": "tx",
                "Source": "mqtt-mzj7aqxk",
                "Status": "ACTIVE"
            }
        ],
        "RequestId": "225d15f3-b60b-4fd7-927a-0c7923eda71f"
    }
}
```

