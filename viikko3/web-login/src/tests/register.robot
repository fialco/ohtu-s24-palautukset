*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Registration Should Fail With Message  Username should be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  makkis
    Set Password  pekkis
    Set Password Confirmation  pekkis
    Submit Credentials
    Registration Should Fail With Message  Password should be at least 8 characters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  makkis
    Set Password  MakkisPekkis
    Set Password Confirmation  MakkisPekkis
    Submit Credentials
    Registration Should Fail With Message  Password shouldn't contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  makkis
    Set Password  M4kk!5P3kk!5
    Set Password Confirmation  M4kk!5P3kk15
    Submit Credentials
    Registration Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Credentials
    Registration Should Fail With Message  User with username kalle already exists 


*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page