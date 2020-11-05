**Example 1: Getting temporary credentials**

This example shows you how to grant temporary credentials with the following permissions:
{"version":"2.0","statement":[{"effect":"allow","action":["name/cos:PutObject"],"resource":["qcs::cos:ap-beijing:uid/123456:prefix//123456/bucketA/*"]}]}

Note: As the GET request url-encodes all parameters, the `Policy` parameter in the following example has been url-encoded twice.

Input: 

```
tccli sts GetFederationToken --cli-unfold-argument  \
    --Name SUN\
    --Policy %7b%22version%22%3a%222.0%22%2c%22statement%22%3a%5b%7b%22action%22%3a%5b%22name%2fqcisa%3aGetInfoByFields%22%5d%2c%22resource%22%3a%5b%22qcs%3a%3aqcisa%3a%3auin%2f90000000000%3aqcisa%2fbigCustomerDetail%22%2c%22qcs%3a%3aqcisa%3a%3auin%2f90000000000%3aqcisa%2fuserDetail%22%2c%22qcs%3a%3aqcisa%3a%3auin%2f90000000000%3aqcisa%2fauthDetail%22%5d%2c%22effect%22%3a%22allow%22%7d%5d%7d
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "Token": "kTRtHpOSOCUzTVWmzlPKweHffXjT9Izo7b61a142d6b56d31c0a7ace4d22bcff3zpbsXKTIrCo43dRRh7bDIKE1ZOE1KRYHEm0KNLjWG_aSF63YoQWchg-l7eXMInxXIc65HqXPjnouCcnQC98J8wEXGfE-X74QQ4kqdZXvvtgJ4yNUyDFRRkgdWtroOk0zQu4Y-h2N6pQU0FyMLSExd3UwGXpNe-CwqgNw9LTMDdz7LwsiQ9QgVCYSBdGaZXH_kOOfbAQFEDzW_8LId2mJG7DNPQMfpvc8pU_uNi0CZuQr686kYm3pLFg09UNHvB5ddn1m5SOBQRfLCK5Esdk4reSu5xw-KdZjJH2U0nZvXPU0JFrRNni1ouUdZiMpXKeZvxiooPMXtyOa_6ZTcdxjOMJfNx6pBOMWnBBJ9ShMV3S6t6AV3QSvCyvwH7dFQBXT9FPY8KK4uqRW168Q2kVt5dDdWqbRHbNg2ofhnUyHRMgYgKhtPFEAj4pJlorgWpyWtGMCGdCqnQkZ-gPOHEG0alJwveCB7CGU-K06cIGA2tZWWVr7wQRF6PrN5hWXnGI-M3hfEy1KX0degBEsjOMD4ORq2OOFvRiROln03wtBwSFCc0IhpYxCiHTsb3IAz69aU8_KEScc3ARNha5wk5L7XmyOaq9PXV5gcmV9Tw4-uO6DFwkgNPWhEyEkNYa8odPaJdrB7y8MVD_XAG92yjd5nuen7TRLCbS_0n2TbaKBZik4B_Pgxxh2QtzHfsqYdPRCzXACvhaIvnRO176cK0cgo4YKe_lTU-eqXuuoy-pqDEY2R_5ERV_UmLts89TgWVFPSGRJTQHFmLQ8RuGugenUP063kE_vAgtu0JWYn09sm1cjzJcG6E1ZJgJEWhB3LsUuhLuYn3HtwK6R65e4c3D0YKYiTzFdv3jK9aGlowL56Gfujkf2k5jX01JOltIFxotyKO2nBAD2to-7ExwvhhbTbBW-P5WpvoSqC86hdBxzAKgdJV-AHG0wKu8kHjO9w0DvT8IufPp8TbdcqFSUFhkEO5xXX4doDsjrSzW3qjnxQ6pDqkYW_kd41U-UwYbdNBoc0jsEtDCwW5UV2l2E6I0zFdML-68lUN3y0vrnaySxLxPt44t8BZDSoMpPgVyxEonyD6zarPWsFLvZGOwsCI4thDZ6jvud0KIpbQn0a0jDUsLhA24myxLjFpYbFPK5jqEDL8l5vHrJkvUOvUM4sM7e78FHx_7cIMw0upCBfuIMUd228Rfsz0JlBrIGrfOFg1iNVJ5A7Q1RH0zWR27jbmzr7a3c-g0_Fw9I8Bb3GdFD1vRhPpvARKXJHFHNSaausuwUu2_yHyvlMpXPUg3i9YVkQxO1aeEE6aH5RZSVKkqbt3ysxxv4OkhUaEuERQy-AEIuiu10Y79EbvjA6GQ0cotsl-gS5FIy54DbcEz5QEQ2gUtMa_IZjyLVPVAVvY8aqj3L2M9_xBIrV_nZ3BGFrn5FfkXUmImzl0kya6Mx_RwvVya7_triXDXTlUPM-JnMrjDkVP_bQNS2EU-61J8ibqj9Yvt4MoO8xojTbQKg9z_xN6jxRuoHeGslrQNSDtKu8uCWKMZNs78PPDmSrEkdwNOPENLPtfy_si32HV7jr3NxEHpyEin0sYOwKuUxJ9XovRVnw_-x9vQy7Duaqb4Ej0pGgvwB-B0WpVO80cFz-131ee7CkYNpqjJljRBUNdvmYHd_QYKQU1WwD8xXrRIQ7d4RsXbzOutl5yb2MxGcpLC5qS62cG6b1XeLSO5h1ZtsFte69kwwTk_fr4zHgqUxrMXjPMRKXKIWFoKGlt6Aycj4ezNkUsoO9pTPCbo0gfMLvWEEvP009_QRI0k6Vby-CKkufjnh3cAGJzpbHUaSxNNp7oN-DDx4O1om4wsiKeMQb-O1y8ZF6HrXYsjaNlJ61EfqHYFGv6tgf_hgGIeppNZMIPvG1YxlTHjykBTxacK1FY0GwtcujQjXY2cFTNFG7hYOgvdJ4ZKzB4HfpB6xIv8v8mFaqZb4dM0ng4KRfQDmq2CUdamJA9MTCU5jTJfNUnGy7M0DCwJMQZRlOmUaVMzKTWkHCnBXEJAgOd3nzYXug3xAKTGKPtcsvoJKM1XawG2-EWPRFAaVn11wThx-SRLcZakynQsu_9VgWiE4qdoSVUGmjExw6vqjqkbiuizZ5zPzzC9cZkwtfoGkdR9DzMmf5etNrGmKJgvJBuNwUWlMJb7m",
            "TmpSecretId": "AKIDw7dwZbmFSup9CnAOraJ7skiPMybaV3WPP5B4oVMCIL5kLyphV_3IyAHFJ5QMCjE6",
            "TmpSecretKey": "/lvEo280/AlGt4orjDl9tWLIOMl5nkexS5Pg+xys7ps="
        },
        "ExpiredTime": 1547696355,
        "RequestId": "59a5e07e-4147-4d2e-a808-dca76ac5b3fd"
    }
}
```

