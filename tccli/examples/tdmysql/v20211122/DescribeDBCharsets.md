**Example 1: 查询字符集**



Input: 

```
tccli tdmysql DescribeDBCharsets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CharsetCollations": [
            {
                "CharsetName": "UTF8",
                "Collations": [
                    "UTF8_GENERAL_CI",
                    "UTF8_BIN",
                    "UTF8_CROATIAN_CI",
                    "UTF8_CZECH_CI",
                    "UTF8_DANISH_CI",
                    "UTF8_ESPERANTO_CI",
                    "UTF8_ESTONIAN_CI",
                    "UTF8_GENERAL_MYSQL500_CI",
                    "UTF8_GERMAN2_CI",
                    "UTF8_HUNGARIAN_CI",
                    "UTF8_ICELANDIC_CI",
                    "UTF8_LATVIAN_CI",
                    "UTF8_LITHUANIAN_CI",
                    "UTF8_PERSIAN_CI",
                    "UTF8_POLISH_CI",
                    "UTF8_ROMAN_CI",
                    "UTF8_ROMANIAN_CI",
                    "UTF8_SINHALA_CI",
                    "UTF8_SLOVAK_CI",
                    "UTF8_SLOVENIAN_CI",
                    "UTF8_SPANISH2_CI",
                    "UTF8_SPANISH_CI",
                    "UTF8_SWEDISH_CI",
                    "UTF8_TOLOWER_CI",
                    "UTF8_TURKISH_CI",
                    "UTF8_UNICODE_520_CI",
                    "UTF8_UNICODE_CI",
                    "UTF8_VIETNAMESE_CI"
                ],
                "DefaultCollation": "UTF8_GENERAL_CI"
            },
            {
                "CharsetName": "GBK",
                "Collations": [
                    "GBK_CHINESE_CI",
                    "GBK_BIN"
                ],
                "DefaultCollation": "GBK_CHINESE_CI"
            },
            {
                "CharsetName": "LATIN1",
                "Collations": [
                    "LATIN1_SWEDISH_CI",
                    "LATIN1_BIN",
                    "LATIN1_DANISH_CI",
                    "LATIN1_GENERAL_CI",
                    "LATIN1_GENERAL_CS",
                    "LATIN1_GERMAN1_CI",
                    "LATIN1_GERMAN2_CI",
                    "LATIN1_SPANISH_CI"
                ],
                "DefaultCollation": "LATIN1_SWEDISH_CI"
            },
            {
                "CharsetName": "UTF8MB4",
                "Collations": [
                    "UTF8MB4_0900_AI_CI",
                    "UTF8MB4_GENERAL_CI",
                    "UTF8MB4_0900_AS_CI",
                    "UTF8MB4_0900_AS_CS",
                    "UTF8MB4_0900_BIN",
                    "UTF8MB4_BIN",
                    "UTF8MB4_CROATIAN_CI",
                    "UTF8MB4_CS_0900_AI_CI",
                    "UTF8MB4_CS_0900_AS_CS",
                    "UTF8MB4_CZECH_CI",
                    "UTF8MB4_DA_0900_AI_CI",
                    "UTF8MB4_DA_0900_AS_CS",
                    "UTF8MB4_DANISH_CI",
                    "UTF8MB4_DE_PB_0900_AI_CI",
                    "UTF8MB4_DE_PB_0900_AS_CS",
                    "UTF8MB4_EO_0900_AI_CI",
                    "UTF8MB4_EO_0900_AS_CS",
                    "UTF8MB4_ES_0900_AI_CI",
                    "UTF8MB4_ES_0900_AS_CS",
                    "UTF8MB4_ES_TRAD_0900_AI_CI",
                    "UTF8MB4_ES_TRAD_0900_AS_CS",
                    "UTF8MB4_ESPERANTO_CI",
                    "UTF8MB4_ESTONIAN_CI",
                    "UTF8MB4_ET_0900_AI_CI",
                    "UTF8MB4_ET_0900_AS_CS",
                    "UTF8MB4_GERMAN2_CI",
                    "UTF8MB4_HR_0900_AI_CI",
                    "UTF8MB4_HR_0900_AS_CS",
                    "UTF8MB4_HU_0900_AI_CI",
                    "UTF8MB4_HU_0900_AS_CS",
                    "UTF8MB4_HUNGARIAN_CI",
                    "UTF8MB4_ICELANDIC_CI",
                    "UTF8MB4_IS_0900_AI_CI",
                    "UTF8MB4_IS_0900_AS_CS",
                    "UTF8MB4_JA_0900_AS_CS",
                    "UTF8MB4_JA_0900_AS_CS_KS",
                    "UTF8MB4_LA_0900_AI_CI",
                    "UTF8MB4_LA_0900_AS_CS",
                    "UTF8MB4_LATVIAN_CI",
                    "UTF8MB4_LITHUANIAN_CI",
                    "UTF8MB4_LT_0900_AI_CI",
                    "UTF8MB4_LT_0900_AS_CS",
                    "UTF8MB4_LV_0900_AI_CI",
                    "UTF8MB4_LV_0900_AS_CS",
                    "UTF8MB4_PERSIAN_CI",
                    "UTF8MB4_PL_0900_AI_CI",
                    "UTF8MB4_PL_0900_AS_CS",
                    "UTF8MB4_POLISH_CI",
                    "UTF8MB4_RO_0900_AI_CI",
                    "UTF8MB4_RO_0900_AS_CS",
                    "UTF8MB4_ROMAN_CI",
                    "UTF8MB4_ROMANIAN_CI",
                    "UTF8MB4_RU_0900_AI_CI",
                    "UTF8MB4_RU_0900_AS_CS",
                    "UTF8MB4_SINHALA_CI",
                    "UTF8MB4_SK_0900_AI_CI",
                    "UTF8MB4_SK_0900_AS_CS",
                    "UTF8MB4_SL_0900_AI_CI",
                    "UTF8MB4_SL_0900_AS_CS",
                    "UTF8MB4_SLOVAK_CI",
                    "UTF8MB4_SLOVENIAN_CI",
                    "UTF8MB4_SPANISH2_CI",
                    "UTF8MB4_SPANISH_CI",
                    "UTF8MB4_SV_0900_AI_CI",
                    "UTF8MB4_SV_0900_AS_CS",
                    "UTF8MB4_SWEDISH_CI",
                    "UTF8MB4_TR_0900_AI_CI",
                    "UTF8MB4_TR_0900_AS_CS",
                    "UTF8MB4_TURKISH_CI",
                    "UTF8MB4_UNICODE_520_CI",
                    "UTF8MB4_UNICODE_CI",
                    "UTF8MB4_VI_0900_AI_CI",
                    "UTF8MB4_VI_0900_AS_CS",
                    "UTF8MB4_VIETNAMESE_CI",
                    "UTF8MB4_ZH_0900_AS_CS"
                ],
                "DefaultCollation": "UTF8MB4_0900_AI_CI"
            },
            {
                "CharsetName": "GB18030",
                "Collations": [
                    "GB18030_CHINESE_CI",
                    "GB18030_BIN",
                    "GB18030_UNICODE_520_CI"
                ],
                "DefaultCollation": "GB18030_CHINESE_CI"
            },
            {
                "CharsetName": "UJIS",
                "Collations": [
                    "UJIS_JAPANESE_CI",
                    "UJIS_BIN"
                ],
                "DefaultCollation": "UJIS_JAPANESE_CI"
            },
            {
                "CharsetName": "EUCKR",
                "Collations": [
                    "EUCKR_KOREAN_CI",
                    "EUCKR_BIN"
                ],
                "DefaultCollation": "EUCKR_KOREAN_CI"
            }
        ],
        "RequestId": "846e328b-e6c6-4e0d-bd6e-bb58bb36ebdf"
    }
}
```

