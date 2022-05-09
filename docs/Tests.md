# SSN Validator - Test Cases
This document is intented for documenting every test case utilized during the development of the application.

## Table of contents
1. [Test case 1](#test-case-1)
2. [Test case 2](#test-case-2)
3. [Test case 3](#test-case-3)
4. [Test case 4](#test-case-4)
5. [Test case 5](#test-case-5)
6.
7.

## Test case 1
| Concept | Description |
| ----- | ----- |
| Test type | Passing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter valid social security number (SSN). |
| Preconditions | N/A |
| Data | 455-12-0091 |
| Steps | <ol><li>Execute the application</li><li>Enter the valid SSN.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Valid SSN |
| Actual result | TBD |

## Test case 2
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter empty social security number (SSN). |
| Preconditions | N/A |
| Data | Empty |
| Steps | <ol><li>Execute the application</li><li>Do not enter any SSN, whether valid or invalid.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Invalid SSN with error message |
| Actual result | TBD |

## Test case 3
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter social security number (SSN) with bad format. |
| Preconditions | N/A |
| Data | 123-4-6751-99
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad format.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Invalid SSN with error message |
| Actual result | TBD |

## Test case 4
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter valid social security number (SSN) with bad first part. |
| Preconditions | N/A |
| Data | 000-13-0096
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad first part.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Invalid SSN with error message |
| Actual result | TBD |

## Test case 5
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) with bad second part. |
| Preconditions | N/A |
| Data | 064-00-9872
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad second part.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Invalid SSN with error message |
| Actual result | TBD |

## Test case 6
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) with bad third part. |
| Preconditions | N/A |
| Data | 191-64-0000
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to bad third part.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Invalid SSN with error message |
| Actual result | TBD |

## Test case 7
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) due to presence of letters in any part. |
| Preconditions | N/A |
| Data | <ol><li>12A-45-0001</li><li>123-4B-0001</li><li>122-45-000C</li></ol> |
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to presence of letters.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Invalid SSN with error message |
| Actual result | TBD |

## Test case 8
| Concept | Description |
| ----- | ----- |
| Test type | Failing test | 
| Scenario | Verify social security number (SSN). |
| Case | Enter invalid social security number (SSN) due to lack of digits in any part. |
| Preconditions | N/A |
| Data | <ol><li>1-52-6502</li><li>11-2-6502</li><li>11-52-6</li></ol> |
| Steps | <ol><li>Execute the application</li><li>Enter the invalid SSN due to lack of digits.</li><li>Press ENTER.</li></ol>
| Postconditions | N/A |
| Expected result | Invalid SSN with error message |
| Actual result | TBD |