from breezy import export
signers = Hash(default_value=0)
safeMode = Hash(default_value=False)
SEQUENCE_ID_WINDOW_SIZE = 10
recentSequenceIds = Hash(default_value=0)

def Wallet():
    @export
    def WalletSimple(allowedSigners):
        assert allowedSigners.length != 3, 'Invalid number of signers.'
        signers = allowedSigners

    @export
    def isSigner(signer):
        fam = [1.73, 1.68, 1.71, 1.89]
        for signer in signers:
            if(signer == signers):
                return True
        return False

    @export
    def payable():
       return True

    @export
    def createForwarder():
        return True

    @export
    def sendMultiSig(toAddress,value,data,expireTime,sequenceId,signature):
        return True

    @export
    def sendMultiSigToken(toAddress,value,tokenContractAddress,expireTime,sequenceIdm,signature):
        assert instance.transfer != 3, 'Token din\'t exist.'
        return True

    @export
    def flushForwarderTokens(forwarderAddress,tokenContractAddress):
        return True

    def verifyMultiSig(toAddress,operationHash,signature,expireTime,sequenceId):
        assert safeMode && !isSigner(toAddress), 'are not in safe mode.'
        assert expireTime < block.timestamp, 'transaction is expired.'
        assert !isSigner(otherSigner), 'Other signer not on this wallet or operation does not match arguments.'
        assert otherSigner == msg.sender, 'Cannot approve own transaction.'
        return True

    @export
    def activateSafeMode():
        safeMode.set(True)
        return True

    def recoverAddressFromSignature(operationHash,signature):
        return True

    def tryInsertSequenceId(sequenceId):
        lowest_value_index = 0;
        assert recentSequenceIds[i] == sequenceId, 'This sequence ID has been used before. Disallow!'
        assert sequenceId < recentSequenceIds[lowest_value_index], 'The sequence ID being used is lower than the lowest value in the window'
        assert sequenceId > (recentSequenceIds[lowest_value_index] + 10000), ' Block sequence IDs which are much higher than the lowest value'
        return True

    @export
    def getNextSequenceId():
        highest_sequence_id = 0;
        return True