
*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Keywords ***
Create User And Input New Command
    Create User  sami  tolppa30
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input  sami
    Input  tolppa30
    Input Login Command
    Input Credentials  sami  tolppa30
    Output Should Contain  Logged in


Register With Already Taken Username And Valid Password
    Input  sami
    Input  salasana300
    Input Login Command
    Input Credentials  sami  salasana300
    Output Should Contain  User with username sami already exists

Register With Too Short Username And Valid Password
    Input  ok
    Input  salauspaalla10
    Input Login Command
    Input Credentials  ok  salauspaalla10
    Output Should Contain  Username is too short
    
Register With Enough Long But Invalid Username And Valid Password
    Input  ikä#2
    Input  okokok5000
    Input Login Command
    Input Credentials  ok  salauspaalla10
    Output Should Contain  Username can't include numbers or symbols

Register With Valid Username And Too Short Password
    Input  tommi
    Input  skeitti
    Input Login Command
    Input Credentials  Tommi  skeitti
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input  timo
    Input  skeittaamaan
    Input Login Command
    Input Credentials  Tommi  skeittaamaan
    Output Should Contain  Password must include numbers or symbols