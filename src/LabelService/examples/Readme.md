# DHL API Interface:

To request an label, POST /

https://entwickler.dhl.de/group/ep/wsapis/retouren/operationen#/Returns/post_


Required parameters (body):
```
{
  "receiverId": "DE",
  "customerReference": "string",
  "shipmentReference": "string",
  "senderAddress": {
    "name1": "string",
    "name2": "string",
    "name3": "string",
    "streetName": "string",
    "houseNumber": "string",
    "postCode": "12345",
    "city": "string",
    "country": {
      "countryISOCode": "string",
      "country": "string",
      "state": "string"
    }
  },
  "email": "user@example.com",
  "telephoneNumber": "string",
  "weightInGrams": 0,
  "value": 0,
  "customsDocument": {
    "currency": "EUR",
    "originalShipmentNumber": "string",
    "originalOperator": "string",
    "acommpanyingDocument": "string",
    "originalInvoiceNumber": "string",
    "originalInvoiceDate": "string",
    "comment": "string",
    "positions": [
      {
        "positionDescription": "string",
        "count": 0,
        "weightInGrams": 0,
        "values": 0,
        "originCountry": "string",
        "articleReference": "string",
        "tarifNumber": "string"
      }
    ]
  },
  "returnDocumentType": "SHIPMENT_LABEL"
}
```

If successful, it returns code **201** and the following response: 

```
{
  "shipmentNumber": "string",
  "labelData": "string",
  "qrLabelData": "string",
  "routingCode": "string"
}
```

Now this is where the fun happens! **labelData** and **qrLabelData** are strings Base64 coded that store the img/pdf file.

We only have to store this data and can directly use this in our html tags! Hurray!


<details>
<summary> Here is an example to display a base64 img in html, QR-label</summary>

```
// In your < img > add the string to src

img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAc ..."
```

Example:

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcIAAAHCCAYAAAB8GMlFAAAaO0lEQVR4nO3d25LbOhIlUHpi/v+XPQ8nKtpj1wVVAomdmWs9ltUgkQCZ4pG0+9fv379/XwAw1P85fQIAcJJGCMBoGiEAo2mEAIymEQIwmkYIwGgaIQCjaYQAjKYRAjCaRgjAaBohAKNphACMphECMJpGCMBoGiEAo2mEAIymEQIwmkYIwGgaIQCjaYQAjKYRAjCaRgjAaBohAKNphACMphECMJpGCMBoGiEAo2mEAIymEQIwmkYIwGgaIQCjaYQAjKYRAjCaRgjAaBohAKNphACMphECMJpGCMBoGiEAo/3f0yfwil+/fp0+hVv9/v379CkAm7hf5fr1u+DZd99Qf9u1RH/X7aNxV1+Xbvc8TtVv2nF3Oz0P96t8pRrhtA31t1eW6qPa/T3m6uvS7Z7HqfpNO+5uJ+fhfpWxB1aU+Yxw+qa6rp/X4LP/3Z//tvq6dLvncap+046728l5JMz/tEo1KNMIAeAOJRphpXcWd1MLyOYa/Z8qtSjRCAHgLvGNsMo7iid9tyaffWj957+tvi7d7nmcqt+04+52Yh7uV/+qUJP4Rsge713Qr/wt3e55nKrftOPu1mUe3Cv+5xMV3k2cEL5sMJL71fvS71elk2VWpS2CiwX4iPvV81o3wrQN9ebtvJ7eYKeSR3aPl/66VV2Oezq5ZZfT55dWjzen7ldPavkZ4e/fv2M31Z+ePM/3NvErG/vUeOl/W9XluKfmsdvJ83O/Oq9dI6y4UHef86nkkd3jpb9uVZfjTkuguYP7VYZ2jRAAvqNVI6z8TqXyuQPfV/mar3zu72nVCAHgu9o0wg7vUO6aw6nkkd3jpb9uVZfjTkugeeqYVXSYw5s2jZDPnUoe2T1e+t9WdTlul+SW9PPjXm2SZcKnsWzafKGTaddvl/m2/kH9d736Ven0xQb6cL/aRyO89v1W6G2c1A02LaEkPUmny3HT69wl+ebNlPvVk0Z/Rvjr169bfjB717ivmJZQkp6k0+W46XXuknxzXbPuV08b2whP3UxOmJZQkp6k0+W46XXuknxzXbPuVyeMbYQAcF1DG+GT73wmv8sCXud+db+RjRAA3oxrhCfe8Zx+lzUtoSQ9SafLcdPr3CH5ZuL96oRxjXCqaQkl6Uk6XY6bXucuyTfcy+8IB9l9Ya+Ol/66VadujOnHTa/zqXlQhydCAEbzREg56Qk0q9ITWU4dt0uiDXV4IqSU9ASaVemJLKeO2yXRhlo0QspIT6BZlZ7Icuq4XRJtqEcjBGA0jRCA0TRCAEbTCCkjPYFmVXoiy6njdkm0oR6NkFLSE2hWpSeynDpul0QbavE7QspJT6BZlZ7Icuq4XRJtqMMTIQCjeSIcpEsCyKr08zslfR9IluFpngiH6JIAsir9/E5J3weSZThhXCM88S7v9DvLLgkgq9LP75T0fSBZ5l8T71cnjGuEAPCnkY3wyXc8E99dAfu4X91vZCMEgDdjG+GpHxuf0CUBZFX6+Z2Svg8ky3xs0v3qhLGN8Lr+W/g7Fv+ucV/RJQFkVfr5nZK+DyTLfGzS/eppv36HV2D1W1s7pvHqN8SePIfwZYOR3K/uO9ad/KD+D+mLBfDG/WofjZB/pCd7TEuMmZbMk35c+hn9GSH/Sk/2mJYYMy2ZJ/249NSmEXbYtKfnkJ7sMS0xZloyT/pxd6q0Dz/SYQ5v2jRCAPiJVo2w8juUyucOfF/la77yub+nVSMEgO9q1wgrvlNJOef0ZI9piTHTknnSj3uHlGv/Oyqe81faNcLr+m+hKixW4nmmJ3tMS4yZlsyTftw7JN4H3lPlPH+iTbLMZ9Km2HFOQM9ru+Oc/jbiB/Vd38UA/bhfPW9EI+Q/6UkcxjNep/Goo+VnhPwrPYnDeMbrNB61xDdC78r+9d2apCdxGM94XcZzv/pXhZrEN0IAuFOJRljhHcVT1AKyuUb/p0otSjRCALhLmUZY5Z3FnX5ag/QkDuMZr9N4r/zvOqlUg/gf1L9n2re5di1R+tfNjWe8TuN9NG53BVtKzUb4pvsGK7w0wF/cr3KVboQA8CrJMtxuWmLH6nzT65L+nx671JnzynxZhpqmJXaszje9LunJLV3qTAaNkNvsTgBJtzrf9LokJ7d8Z7z0OpNDIwRgNI0QgNE0QgBG0wi5zR2JHclW55tel/Tkli51JodGyK3eu+F0vgmtzje9LrvP79R46XUmgx/UAzCaJ0IARiuVLHMqIWJ3gkX6605JX98u0vdL+vWRXpfd46XXZYcyT4SnEiJ2J1ik/+2U9PXtIn2/JF0LFeuye7z0uuxSohGeSojYnWCR/rpT0te3i/T9kn59pNdl93jpddmpRCMEgLtohACMphECMFqJRngqIWJ3gkX6605JX98u0vdL+vWRXpfd46XXZacSjfC6ziVE7E6wSP/bKenr20X6fkm6FirWZfd46XXZRbIMAKOVeSIEgDuUSpbZrUtCxO7jpidEdKlfep13m1a/U/NIHy/R2CfCLgkRu4+bnhDRpX7pdd5tWv1OzSN9vFQjG2GXhIjdx01PiOhSv/Q67zatfqfmkT5espGNEADeaIQAjKYRAjDayEbYJSFi93HTEyK61C+9zrtNq9+peaSPl2xkI7yuPgkRu4+bnhDRpX7pdd5tWv1OzSN9vFSSZQAYbewTIQBcV7FkmfTEiS7JGaeSKdKTONLXI71+p8bbbdp+2X3cRGWeCNMTJ7okZ5xKpkhP4khfj/T6nRpvt2n7ZfdxU5VohOmJE12SM04lU6QncaSvR3r9To2327T9svu4yUo0QgC4i0YIwGgaIQCjlWiE6YkTXZIzTiVTpCdxpK9Hev1OjbfbtP2y+7jJSjTC68pPnOiSnHEqmSI9iSN9PdLrd2q83abtl93HTSVZBoDRyjwRAsAdJMtslH7c9PqtSq/z7vHS163L+aWPl54Yk37f+EyZJ8IuiQ6njptev1Xpdd49Xvq6dTm/9PHSE2PS7xtfKdEIuyQ6nDpuev1Wpdd593jp69bl/NLHS0+MSb9vrCjRCAHgLhohAKNphACMVqIRdkl0OHXc9PqtSq/z7vHS163L+aWPl54Yk37fWFGiEV5Xn0SHU8dNr9+q9DrvHi993bqcX/p46Ykx6feNr0iWAWC0Mk+EAHCHlskyp8bbLT3RIf38VqUne+x2ar7pddlt2nVZeX3LPBGmJ0Tslp7okH5+q9KTPXY7Nd/0uuw27bqsvr4lGmF6QsRu6YkO6ee3Kj3ZY7dT802vy27TrssO61uiEQLAXTRCAEbTCAEYrUQjTE+I2C090SH9/FalJ3vsdmq+6XXZbdp12WF9SzTC68pPiNgtPdEh/fxWpSd77HZqvul12W3adVl9fSXLADBamSdCALhDqWSZU9ITGE6NJ3mEO9h/70tPjEmv32c8EX4hPYHh1HiSR7hD0l5L2n/piTHp9fuKRviJ9ASGU+NJHuEO9t/3zyEhMSa9fis0QgBG0wgBGE0jBGA0jfAT6QkMp8aTPMId7L/vn0NCYkx6/VZohF9IT2A4NZ7kEe6QtNeS9l96Ykx6/b4iWQaA0TwRAjBaqWSZLkkS6ckZXZJvqjr926vv1nPa/jt1XHW+T5knwi5JEkkpGUnJFKfG4zXT9t+p46rzvUo0wi5JEunJGV2Sb3jGtP136rjqfL8SjRAA7lLqM0LoKO1dc+XPeuAnPBECMFqJRtglSSI9OaNL8g3PmLb/Th1Xne9XohFeV58kiaSUjKRkilPj8Zpp++/UcdX5XpJl4LCvPiP8+xJ9+jNFtwi6K/NECAB3KPWt0S5JCF0SJyRYcF3z1qPL9ZE+jyeVeSLskoTQJXFCggXXNW89ulwf6fN4WonPCL/7GcrT45067up46a9bdWrd7pZ+w1h9Alj931XV5fpIn8cJZZ4IAeAOGiEAo2mEAIxWohF2SULokjghwYLrmrceXa6P9HmcUKIRXlefJIQuiRMSLLiueevR5fpIn8fTSnxrFDqr+q1R6KLMEyEA3EGyzMbxdks/v1XT1o33TUtQSU9uST+/J5V5IpyWUJJ+fqumrRvvm5agkp7ckn5+TyvRCD8r6E+KvXu83dLPb9W0deN9p/bBtNetSj+/E0o0QgC4S6nPCIGvVfpsBhJ4IgRgtBKNcFpCSfr5rZq2brxvWoJKenJL+vmdUKIRXte8hJL081s1bd1437QElfTklvTze5pkGTjs9Dfr3AKYrswTIQDcodS3RrskHHRJiDhV5/T1nabLPkgfb7f083tSmSfCLgkHXRIiTtU5fX2n6bIP0sfbLf38nlbiM8KvFuhtCquvO2X3+e2uS3qdf3rctHe+u284p+ZTbR9UHW+39PM7ocwTIQDcQSMEYDSNEIDRSnxGeF0f/3ftv09/9XWn7D6/3XVJr/NPjvv0Z4RPf+ng5N6utA8qj7db+vk9rcwTYZeEgy4JEafqnL6+03TZB+nj7ZZ+fk8r80QIP+WJEPhMmSdCALhDqWSZVV0SIk4lvKSP96q75/e0Kr8L67KfTx132nhPavdE2CUh4lTCS/p41NRlP5867rTxntaqEX5W+J8syu7xdh83fb6n6keWLvv51HGnjXdCq0YIAN/V8jNC+I7vfraR9i539TeewPs8EQIwWqtG+Nk7+Z98g2n3eLuPmz7fU/UjS5f9fOq408Y7oVUjvK4+CRGnEl7Sx6OmLvv51HGnjfc0yTK01/0zM5cwvKbdEyEAfEepb42eSqboYnf91JnrOpdQkp4YM+16Sz+/z5R5IjyVTNHF7vqpM9d1LqEkPTFm2vWWfn5fKdEITyVTdLG7furMdZ1LKElPjJl2vaWf34oSjRAA7qIRAjCaRgjAaGV+R/jRf2tezVksMs3b7K5f5TpX+dziI0k13r0P0vffqeso/XpLP7+vlHkiPJVM0cXu+qkz13UuoSQ9MWba9ZZ+fl8p80QIu3giBP5U5okQAO4gWeaA9Hl0qd9H/P/37ZW+T09db13Ob4IyT4TTEhjSkzNOST+/adL36anrrcv5TVGiEU5LYEhPzjgl/fymSd+np663Luc3SYlGCAB3KfUZIdwh/TPDyZ/dwBM8EQIwWolG+Nk74j//bfV1p6TPo0v9eEb6Pj11vXU5v0lKNMLrmpfAkJ6ccUr6+U2Tvk9PXW9dzm8KyTLwhac/M3RJwrPKPBECwB1KfWv0VFJDekLEbulJIdTkentNerJM5TqXeSI8ldSQnhCxW3pSCDUlXVsV91V6skz1Opf4jPCrgr5NocvrTjl1ful1+dt3L/Dv/k4xbb6vcr29Zvc80sc7ocwTIQDcQSMEYDSNEIDRSnxGeF0f/3fo1c9fqr3ulFPnl16XP939GUvinF/lenvN7nmkj/e0Mk+Ep5Ia0hMidktPCqGmpGur4r5KT5apXucyT4SQwhMh9FLmiRAA7lAqWeaUUwkM6ckPkkIyjn/atH26W3r9JvBE+IVTCQzpyQ9JqSCVEiy6mbZPd0uv3xQa4Sc+20A/2Vyr45067u7xTr2OZ0zbp7ul128SjRCA0XxGCC/yGQ/U5okQgNE0wk989k78J+/SV8c7ddzd4516Hc+Ytk93S6/fJBrhF04lMKQnPySlgrjIz5m2T3dLr98UkmUAGM0TIQCjjf7WaPfEk7+lzyO9frwv/TrqMl766yob+0Q4LfEkfR7p9eN96ddRl/HS/1bdyEY4LfEkfR7p9eN96ddRl/HSX9fByEYIAG80QgBG0wgBGG1kI5yWeJI+j/T68b7066jLeOmv62BkI7yueYkn6fNIrx/vS7+OuoyX/rfqJMsAMNrYJ0IAuK5iyTLpCRG7pZ/fqvREkS77qkvySHr9Th23y/0gUZknwvSEiN3Sz29VeqJIl32VlDLSuX6njtvlfpCqRCNMT4jYLf38VqUninTZV12SR9Lrd+q4Xe4HyUo0QgC4i0YIwGgaIQCjlWiE6QkRu6Wf36r0RJEu+6pL8kh6/U4dt8v9IFmJRnhd+QkRu6Wf36r0RJEu+yopZaRz/U4dt8v9IJVkGQBGK/NECAB3aJksMy2BoUtdpiWUpK9betJP+n5JX7f0+8GTyjwRSmB4X5e6TEsoSV+39KSf9P2Svm7p94OnlWiEEhje16Uu0xJK0tctPeknfb+kr1v6/eCEEo0QAO6iEQIwmkYIwGglGqEEhvd1qcu0hJL0dUtP+knfL+nrln4/OKFEI7wuCQwf6VKXaQkl6euWnvSTvl/S1y39fvA0yTIAjFbmiRAA7jA6WaZLckaXRIxV6vea9OSR9HVLP276+SUq80TYJZmiyzxOUb/XpCePpK9b+nHTzy9ViUbYJZmiyzxOUb/XpCePpK9b+nHTzy9ZiUYIAHfRCAEYTSMEYLQSjbBLMkWXeZyifq9JTx5JX7f046afX7ISjfC6+iRTdJnHKer3mvTkkfR1Sz9u+vmlkiwDwGhlnggB4A4tk2VOHXdCAsOfuqzHqePaL1n7Zfd46ft0t8r7tMwTYZeki+oJDG+6rMep49ovWftl93jp+3S36vu0RCPsknTRIYHhuvqsx6nj2i9r/5Z23PT17VLnE0o0QgC4i0YIwGgaIQCjlWiEXZIuOiQwXFef9Th1XPtl7d/Sjpu+vl3qfEKJRnhdfZIuqicwvOmyHqeOa79k7Zfd46Xv092q71PJMgCMVuaJEADuMDpZJj2BIf11q4xnvJOvW5U+j/QkIskyD5iWwJD+t1XGM97Jv61KOuekuqySLPOAaQkM6a9bZTzjnXzdqvR5nKrLKskyAFCcRgjAaBohAKOVaITTEhjSX7fKeMY7+bpV6fNITyKSLPOgaQkM6X9bZTzjnfzbqqRzTqrLKskyAFBYmSdCALhDqWQZXtMlsSNd+nzTk2pOSZ9H+rql1+8zngiH6JLYkS59vulJNaekzyN93dLr9xWNcIAuiR3p0uebnlRzSvo80tctvX4rNEIARtMIARhNIwRgNI1wgC6JHenS55ueVHNK+jzS1y29fis0wiG6JHakS59velLNKenzSF+39Pp9RbIMAKOV/kF9la/m/pT3KAD3K9kIuzfAN2/z3NUQ0xNPVnVJyOmyHqvS6zJtvN3HrbxPS/2n0SkN8COvLNVHtft7zNXXnXJqHruP22U9VqXXZdp4u49bfZ+W+bLM9CZ4XT+vQXriyaouCTld1mNVel2mjbf7uB32aZlGCAB3KNEIq7yreIJaAOxVohECwF3iG6EnoH99tybpiSeruiTkdFmPVel1mTbe7uN22KfxjZA90hNPVnVJyOmyHqvS6zJtvN3Hrb5P438+4YnwfeHLBlBGyR/Uf1da09DcAXK0boRpDfDN23k93RDTky4kZ7xPIktWItApXfZfopafEf7+/bvEIjx5nu813Vcacfp4u4/b5fzS1+3UeKfWd1WX/ZeqXSOs0AD/diom6at/qzre7uN2Ob/0dUtPBDqly/5L1q4RAsB3tGqEFZ8G31Q+d4DKWjVCAPiuNo2wwxPVXXNIT7qQnPH9sSWy7BsvPRmly/5L1qYR8rn0pAvJGe+TyJKVCHRKl/2Xqk2yTPg0lk2bL8BprX9Q/12vftVXcwKoRyO89v3W5W2c1IaYnjySnmDRpS5d5rEqvc7p+35V+vl9ZvRnhL9+/brlB593jfuK9OSR9ASLLnXpMo9VSTVNqstu6ef3lbGN8NTN84T05JH0BIsudekyj1XpdU7f96vSz2/F2EYIANc1tBE++S6lyjsigKlGNkIAeDOuEZ54Qjv9VJiePJKeYNGlLl3msSq9zun7flX6+a0Y1winSk8eSU+w6FKXLvNYlVTTpLrsln5+XxmXLHPq6Wz3+YUvG0AZnggBGE2yzCCVkx/+1GUeu3VJMkk/bnr9Vk2b72c8EQ5RPfnhTZd57NYlyST9uOn1WzVtvl/RCAfokPxwXX3msVuXJJP046bXb9W0+a7QCAEYTSMEYDSNEIDRNMIBOiQ/XFefeezWJckk/bjp9Vs1bb4rNMIhqic/vOkyj926JJmkHze9fqumzfcrkmUeIlkGIJMnQgBGkyzDP3YnRJwar0tCySnT1i2d/XwfT4T8f3YnRJwar0tCySnT1i2d/XyvcY3wxLuUKu+MdidEnBqvS0LJKdPWLZ39fL9xjRAA/jSyET75hFblaRBgqpGNEADejG2Ep36km2x3QsSp8boklJwybd3S2c/3G9sIr+u/Rbpjoe4a9wm7EyJOjdcloeSUaeuWzn6+17hkmR3HSjiH8GUDKMMP6v+guQDMoxHyj/REkVOvW5WesNElKSR9v6Tvq/T5Pmn0Z4T8Kz1R5NTfVqUnbHRJCknaGxX3Vfp8n9amEVYq+kdOzyE9UeTU61alJ2x0SQpJ3y/p+yp9vie0aYQA8BOtGmGVdx/vqXzuAJW1aoQA8F3tGmHFJ6uUc05PFDn1ulXpCRtdkkLS90v6vkqf7wntGuF1/ddYUprLZxLPMz1R5NTfVqUnbHRJCknaGxX3Vfp8n9YmWeYzaVPsOCeAqkb8oD7tqQuAHCMaIf+ZlkxxKukiPclEXbL2X/p6nBrvSS0/I+Rf05IpTiVdJKWWJCWAJM0taf+lr8ep8Z4W3wgrvat4yndrMi2Z4lTSRXqSibq89rpVXdbj1HgnxDdCALhTiUboqfB/1AJgrxKNEADuUqYRehL6eQ2mJVOcSrpITzJRl9det6rLepwa74T4H9S/p8oHsLvsWqL0r4d3+Tp3+tf/1SVr/6Wvx6nxnlSyEb7p3hALLw1AGaV/UK9RAPCqMp8RAsAdNEIARtMIARhNIwRgNI0QgNE0QgBG0wgBGE0jBGA0jRCA0TRCAEbTCAEYTSMEYDSNEIDRNEIARtMIARhNIwRgNI0QgNE0QgBG0wgBGE0jBGA0jRCA0TRCAEbTCAEYTSMEYDSNEIDRNEIARtMIARhNIwRgNI0QgNE0QgBG0wgBGE0jBGA0jRCA0TRCAEbTCAEYTSMEYDSNEIDRNEIARtMIARjt/wFebFLVMb8sVQAAAABJRU5ErkJggg==">

</details>
