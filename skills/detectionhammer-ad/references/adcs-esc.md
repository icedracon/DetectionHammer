# AD CS ESC posture review checklist

This is a separate reference index, not an additional count of executed tests. ESC names are research taxonomy, not one-to-one ATT&CK techniques. Obtain approved read-only PKI assessment results, check patch and policy context, and validate the finding with the PKI owner. Do not attempt certificate impersonation, enrollment abuse, relay or privilege escalation.

| Class | Defensive review area |
|---|---|
| ESC1 | Certificate subject identity and enrollment governance |
| ESC2 | Template purpose and issuance governance |
| ESC3 | Enrollment agent governance |
| ESC4 | Template ownership and permissions |
| ESC5 | PKI directory object protection |
| ESC6 | CA subject identity policy |
| ESC7 | CA administrative roles and access reviews |
| ESC8 | HTTP enrollment endpoint protection |
| ESC9 | Certificate security extension and mapping posture |
| ESC10 | Certificate mapping policy |
| ESC11 | RPC enrollment transport protection |
| ESC12 | CA private-key protection and operational controls |
| ESC13 | Certificate issuance policy governance |
| ESC14 | Explicit certificate mapping governance |
| ESC15 | CA patch posture for CVE-2024-49019 and template governance |
| ESC16 | CA-wide security extension policy |

Additional emerging classes such as ESC17 require separate primary-source review before adding a validated mapping; this release does not claim exhaustive ESC coverage.

References: https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates ; https://specterops.io/blog/2021/06/17/certified-pre-owned/ . The mapping index is a draft research aid; not all classes have coverage in the Microsoft assessment page.
