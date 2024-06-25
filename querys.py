
QUERY_BETS = """query BetQuery{
                    bets(input:{queryDay:"xxxx-xx-xxT00:00:00"}){
                    id,
                    createdAt,
                    state,
                    product,
                    isFreeBet,
                    stake
                }
            }"""

QUERY_TRANSACTIONS = """query PaymentQuery{
                            transactions(input:{queryDay:"xxxx-xx-xxT00:00:00"}){
                            id,
                            requestedAt,
                            userId,
                            state,
                            referenceId,
                            externalReferenceId,
                            amount,
                            currencyId,
                            providerId,
                            providerName,
                            paymentMethod,
                            postedBy,
                            postedAt,
                            ipAddress,
                            isCorrection,
                            transactionType
                            }
                            }"""
    
