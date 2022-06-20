
import torch
import torch.nn as nn


class ElasticNet(nn.Module):

    def __init__(
        self,input_dim,output_dim=1,activation='sigmoid'):
        super(ElasticNet,self).__init__()

        self.net=nn.Linear(in_features=input_dim,out_features=output_dim)
        nn.init.kaiming_normal_(self.net.weight)

        

    def forward(self,x):
        x=self.net(x)
        f=nn.Sigmoid()
        x=f(x)
        return x
    def cal_l1_loss(self,w):
        """
        calculate l1 loss
        """
        return torch.abs(w).sum()
    
    def cal_l2_loss(self,w):
        """
        calculate l2 loss
        """
        return torch.square(w).sum()

        


