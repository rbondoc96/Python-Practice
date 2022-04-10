## Game Brainstorming

### Possible Starts
1. You walk into big mansion with your friends and you notice one of them is missing. You hear a gunshot a few rooms away. What do you do?
    - 1 Try to leave the way you came.
    - 2 Go through the closest door in the direction of the gunshot.
    - 3 Convince one of your friends to investigate the gunshot.

2. Buying something at a Moogle's shop


### Possible Ends
1. Death with a reason
2. End B


### Influence Trait

Both player and merchant have an influence trait

On every interaction:
- compare(pInf, mInf)
    - If pInf is greater
        - P -> M (sell): Use max(pSP, )
        - M -> P (buy): 
    - The greater one's sell/buy power is used in calcs
    - Equal? Take the average.
- barter()
    - Gold is exchanged
    - 2 50/50 choices
        - 1 for pInf 
        - 1 for mInf


### Selling and Buying Power

P -> M: price * (SP)
P <- M: price * (BP)

SP in range(0.5, 1.5)
BP in range(0.7, 2)

Ideal Player Scenario
- SP: max(pSP, mSP)
- BP: min(pBP, mBP)

Ideal Merchant Scenario
- SP: min(pSP, mSP)
- BP: max(pBP, mBP)


Player {
    sellPower: 1.5
    buyPower: 0.8
}

Merchant {
    sellPower: 2
    buyPower: 0.6
}


Higher selling power = selling for more money
    - Higher percentage modifier is better

Lower buying power = buying for more money
    - Higher percentage modifier is worse

Lower selling power = selling for less money
    - Lower percentage modifier is worse

Higher buying power = buying for less money
    - Lower percentage modifier is better


Item {
    Price: 100,
    Owner: P2
}

0 <= Influence <= 100

P1 {
    Influence: 10
}

Merchant {
    Influence: 20
}

P1 is buying Item from Merchant
- P1.compare_influence(Merchant)
    - Merchant should win
    - diff = 10
        - Merchant sells at 110% | P1 buys at 110%
        - Merchant buys at 90% | P1 sells at 90%

    - P1 wins (influence = 30)
    - diff = 10
        - P1 buys at 90% | Merchant sells at 90%
        - P1 sells at 110% | Merchant buys at 110%

