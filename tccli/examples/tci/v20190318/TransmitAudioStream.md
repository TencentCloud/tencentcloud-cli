**Example 1: 流式音频分析示例**

一个分片的流式音频分析

Input: 

```
tccli tci TransmitAudioStream --cli-unfold-argument  \
    --Functions.EnableVadInfo true \
    --IsEnd 1 \
    --SeqId 1 \
    --SessionId testforsession \
    --UserVoiceData SUQzBAAAAAAANFRDT04AAAAHAAADQmx1ZXMAVFNTRQAAAA8AAANMYXZmNTguMjMuMTAyAAAAAAAAAAAAAAD%2F81jAAAAAAAAAAAAASW5mbwAAAA8AAAASAAAITAAiIiIiIi8vLy8vLzw8PDw8SUlJSUlJVlZWVlZjY2NjY2NwcHBwcH19fX19fYqKioqKl5eXl5eXpKSkpKSksbGxsbG%2Bvr6%2Bvr7Ly8vLy9jY2NjY2OXl5eXl8vLy8vLy%2F%2F%2F%2F%2F%2F8AAAAATGF2YzU4LjQxAAAAAAAAAAAAAAAAJAOVAAAAAAAACEyULaIpAAAAAAAAAAAAAAD%2F8zjEABOylnQLRigAETO960QQJ6YQQPAYDTk8mTJ0YQIB9yBwCBwk5CEISd5zvIQjHDgoxzoQihwOEnOdyB8Pnf5CEb%2F%2FJ%2F%2Fkb%2F%2FQnIT%2F%2F%2FU4fOQPh84gcf%2F4fdgZFMFAgSI3tbm442AGGmn%2F8zjEEBkKUvpfi1AAfjskBZcKzUvSVbbkBJDYQQjiAjweEh5oMAAxlFw2k%2Bp54rlpkWD5QfurYURx1YQtGGn7mdM%2FVu3Rmq2QIhX7ZWx7%2F5Eex766IzR8OwyFiH5dn1HFKghCWjAD0l4f9zT%2F8zjEChdqDubXyzgA3lYDYbubfXyPI2D4dmug8D4iJZc9%2BYIwaBEHgPBor9R8YU890ucccaexjHjBqIc6aHHqb%2F%2F%2F%2F%2FsjrS1mImg2cCg1BlukfTFxC7PpC5FCF0fiWcCdCWNpdRAMYCcHqZf%2F8zjECxfpUu7%2BC9JQ7YQQxOR%2FiKEMUe%2F8q1hNE2EaKBQxc4SWEQlDQsCbSBBCTuqSolZZPPt2k1GqT2EbsZFLIkRIWmJpQqDAoCDv%2F%2FXtcHDDGBwHAIXU5FPmGNLVf%2BiOUgqkR5AiDr1Jh7X%2F8zjEChc4tvMWFhJoYfXUNMqB1gdU4pPwIZnrP%2F8mYkJKNHVmM3yXQoSVDEkDMWPMUFXJOsEoLFTr1VAYgA1fSthFzQ28abcksWuOkSyg6C3T2tzJkkKEEk6ov3B9BBMDoBg1EgT8ootC24j%2F8zjEDBb62tI6FgpoO5GE3EBgQmkw%2FnMdCMQQDBEPGNstEOdTnssPdbMz5GHyiIt%2F91KWkPHrVXra7LGO1GOdVOlWHOSHj7%2Fpt3%2F%2FbOrO7pd5%2BQ4xxEh5r%2BoRIDoFhAAZ3YAEH%2F%2FNbiyCRBn%2F8zjEDxWystLcwkSoLYJUnMaxF7LRRVWrMAgQElk6CbkRETWhQsuYrHuoyO9Jiy3naZB9Stfr%2F%2F%2F%2F6p2eh7osy0u5m6Svo1%2F%2F7%2Bj0qavNQdVA7UuiGxAMkt2ZuyUSEUFGaDj8M8WuGo1X4IL%2F8zjEFxMQpupcBowKRR5FI6kt9afbPm38SfPJrAKBHikFpXloKkIsWYM%2FrPf6h7cAAuOGA4tNVeydJCsVHlv%2F%2FedqLkssZVj%2F4yVQtUemsMYhKaZhU2gdEzWb7LfwLDzWJbhnMD46pRpWrnX%2F8zjEKRUKBrh8egSarpKOqT66Fa6S9DbaJ2Qxj%2F%2FZL0VSspQrWVAJ4sLg6Iv7dyyICEv%2F%2BmJBZVUufh4SdxCqFKEJQMJ%2BsEqaXtrbx4WzXlB%2F%2BXX%2FmHNikKupO1hAKmGRGFEaELvR15TSsYz%2F8zjEMxRCimwQeETdreatS1Zyq39ktUtf0cBxymbx%2F%2FO1uX63eKCeBMIFArlLCwIjqBWHSamMJzj5FFxgaNAeKxQqKX0Mn%2F7P2KGxYdzo1IbVIixgYLAyeUaBk5PJUZbson4URTW24h0%2FSgf%2F8zjEQQ%2FoRlwUS8wA%2FglgBwOUTVxujFPq2x72dRxP%2FX0L0t2%2F%2Fb9Le36McQdCK4U7PBlrQGCQ7koxmDjEKZUZWOcimEnIHM7OymihAJljbgm4zUpugWnetpkMhEO7Eb9FucQBM2PECMOt0CX%2F8zjEYBS6PmQVSxAARGA%2BfNEEC0UBchAQ935fc3LjCOC2JEQ0q%2Flw6VyDnDQwFAiEw6iBCb%2F5OGknSuXECJkIToYFAoAN%2FGd%2F5DCIDQIOolycL7idg2UDzwGmEoBFAhEOQELf%2FlMnx3lxjRb%2F8zjEbCb7zowBipAA98NlDbgbiFhIuRcdh9MuE%2BXv%2F%2FoLdO3vcuGZPloyNC8alQvlwumyRS%2F%2F%2F1f%2F%2FzU6B4d3%2B222ku2H%2Fw1qUtolGx5YxBokEwPjG02NhBZBMqZBhqRqmnCqFa1MJiNRAAj%2F8zjELxRwdxL%2FyxACaDh92VacCiWgbq3G71JGf%2BUIpjHUJCJmLNDJNzhAa0tjGk4AhiEN21AFmCjjKLLxjmPBALF5Egr2PkYAFBZqG4%2BCFGqGM9i7X%2F2Xhr%2B2xkcnpdFRR7I0aWhqZ2Q%2FwYD%2F8zjEPBSRwr78AYYwgZQkyJMu7X5XZXcQljwcK%2B%2F%2BSKuABOoCVhWb2EHuNarNrHOLkiSscbiJVXtQ5rEialjXoGiym5fnkCY%2BH5KSOUOr7atkZnV2WhRJGv59X81%2F4bTh%2FxqEFHcWL1qesrb%2F8zjESBXx%2BqpcAYY8VoLRMoNSwUHD%2F6nvVh1QVnUBvHPzELNOiKAIKRYeq%2FKwzFC1rcX%2F%2F%2BzMxQdGx8X8KsNw3xryKmqKyKitNsHQAw61VeVWSRU2v%2BGa59a1FQkHXxEJQaDhENCWR9TxKJb%2F8zjETxdh4nQ0CZCEDR6HKzqwaPYbqeWgrDTaxYeCA4Cwfy3%2FllqGTWX8jVrLZ%2BXZPvyyX%2FlkuZGstQyNQwUMGBhHFRUUFuoka%2F6hf2oHs%2FxYXZLCwr%2F%2BukxBTUUzLjEwMKqqqqqqqqqqqqr%2F8zjEUA8hVcGWCAYAqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqo%3D \
    --VocabLibNameList testlib2 \
    --VoiceEncodeType 1 \
    --VoiceFileType 3
```

Output: 
```
{
    "Response": {
        "RequestId": "205ca3bb-aa5d-4df8-97d1-06fa865f70d5",
        "Texts": [
            {
                "TextItem": {
                    "Mbtm": 0,
                    "Metm": 512,
                    "Text": "Hey. ",
                    "TextSize": 5,
                    "Confidence": 0.038818073,
                    "Tag": 0,
                    "Words": [
                        {
                            "Mbtm": 70,
                            "Metm": 430,
                            "Text": "hey",
                            "Wsize": 3,
                            "Confidence": 0
                        }
                    ]
                },
                "Speed": 3.90625,
                "MaxVolume": 0,
                "MinVolume": 0,
                "AvgVolume": 0
            }
        ],
        "VocabAnalysisDetailInfo": null,
        "AsrStat": {
            "TotalDuration": 612,
            "SoundDuration": 512,
            "MuteDuration": 100,
            "VadNum": 1,
            "WordNum": 1,
            "AvgSpeed": 1.953125,
            "MaxVolume": 0,
            "MinVolume": 0,
            "AvgVolume": 0
        },
        "VocabAnalysisStatInfo": null
    }
}
```

