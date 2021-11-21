import random

class Sequence:
    def __init__(self, seq):
        self.seq = seq
        
    def correct(self, seq): 
        if seq is None:
            return True
        for a in seq:
            if not (a in self._dict):
                return False
        return True
    
    def compl(self):
        new_seq = ''
        for a in self.seq:
            new_seq = new_seq + self._dict[a]
        return new_seq
    
    def __mul__(self, other):
        new_seq = [random.choice(pair) for pair in list(zip(self.seq, other.seq))]  
        new_seq = ''.join(new_seq)
        if len(self.seq) > len(other.seq):
            new_seq += self.seq[-(len(self.seq) - len(other.seq)):]
        elif len(other.seq) > len(self.seq):
            new_seq += self.seq[-(len(other.seq) - len(self.seq)):]
        return self.__class__(seq=new_seq)
    
    def __getitem__(self, item):
        raise NotImplementedError
    
    def __add__(self, other):
        raise NotImplementedError


class RNA(Sequence):
    def __init__(self, seq):
        self._dict = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}
        if self.correct(seq) == True:
            super().__init__(seq=seq)
        else:
            raise Exeption
        
    def __repr__(self):
        return self.seq
    
    def __getitem__(self, i):
        return self.seq[i]
    
    def __add__(self, other):
        return RNA(self.seq + other.seq)

    def compl_DNA(self):
        forward = self.compl()
        return DNA(seq = forward)
    
    def __eq__(self, other):
        if self.seq == other.seq:
            return True
        return False

class DNA(Sequence):
    def __init__(self, seq, seq_rev=None): 
        self._dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        if self.correct(seq) and self.correct(seq_rev) == True:
            super().__init__(seq=seq)
        else:
            raise Exeption
        super().__init__(seq=seq)
        self.rev = seq_rev 
        if self.rev is None:
            self.rev = self.compl()
            
    def __repr__(self):
        return repr([self.seq, self.rev])
    
    def __getitem__(self, i):
        return [self.seq[i], self.rev[i]]
    
    def __add__(self, other):
        return DNA(self.seq + other.seq, self.rev + other.rev)
    
    def __eq__(self, other):
        if self.seq == other.seq and self.rev == other.rev:
            return True
        return False

if __name__=='__main__':
    dna = DNA('ATG', 'TAC')
    rna = RNA('UGA')
    dna1 = DNA('GG', 'CC')
    rna1 = RNA('CC')
    print(rna*rna1)
    print(dna*dna1, dna*dna1)
    #print(rna.compl())
    #print(DNA(seq='ACT'))
    #print(rna, rna.compl_DNA())
    #print(rna==rna1)

