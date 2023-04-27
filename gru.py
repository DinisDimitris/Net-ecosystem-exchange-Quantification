import torch.nn as nn
import torch 
import torch.nn.functional as F

### Knowledge guided machine learning implementation using gated recurrent units
### Inspired from https://gmd.copernicus.org/articles/15/2839/2022
class KGML(nn.Module):
    def __init__(self, ninp, nhid, nlayers, nout, dropout):
        super(KGML, self).__init__()
        if nlayers > 1:
            self.gru = nn.GRU(ninp, nhid,nlayers,dropout=dropout)
        else:
            self.gru = nn.GRU(ninp, nhid,nlayers)
        #self.densor1 = nn.ReLU() #can test other function
        self.densor2 = nn.Linear(nhid, nout)
        self.nhid = nhid
        self.nlayers = nlayers
        self.drop=nn.Dropout(dropout)
        self.init_weights()

    def init_weights(self):
        initrange = 0.1 #may change to a small value
        self.densor2.bias.data.zero_()
        self.densor2.weight.data.uniform_(-initrange, initrange)

    def forward(self, inputs, hidden):
        output, hidden = self.gru(inputs, hidden)
        #output = self.densor1(self.drop(output))
        #output = torch.exp(self.densor2(self.drop(output))) # add exp
        output = self.densor2(self.drop(output)) # add exp
        return output, hidden

#bsz should be batch size
    def init_hidden(self, bsz):
        weight = next(self.parameters())
        weight = weight.float()
        return weight.new_zeros(self.nlayers, bsz, self.nhid)
    
def get_ini(x,ind,nout):
    initials=[]
    for i in range(len(ind)):
        initials.append(x[:,:,ind[i]].view(x.size(0),x.size(1),nout[i]))
    return initials

def myloss_mul_sum(output, target,loss_weights):
    loss = 0.0
    nout=output.size(2)
    for i in range(nout):
        loss = loss + loss_weights[i]*torch.mean((output[:,:,i] - target[:,:,i])**2)
    return loss

def Z_norm(X):
    X_mean=X.mean()
    X_std=np.std(np.array(X))
    return (X-X_mean)/X_std, X_mean, X_std

class R2Loss(nn.Module):
    #calculate coefficient of determination
    def forward(self, y_pred, y):
        var_y = torch.var(y, unbiased=False)
        return 1.0 - F.mse_loss(y_pred, y, reduction="mean") / var_y
    
class EarlyStopping:
    def __init__(self, tolerance=5, min_delta=0):
     
        self.tolerance = tolerance
        self.min_delta = min_delta
        self.counter = 0
        self.early_stop = False
     
    def __call__(self, train_loss, validation_loss):
        if (validation_loss - train_loss) > self.min_delta:
            self.counter +=1
            if self.counter >= self.tolerance:
                self.early_stop = True