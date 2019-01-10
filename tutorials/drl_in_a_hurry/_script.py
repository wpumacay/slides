



class QNetwork( nn.Module ) :

    def __init__( self, state_size, action_size, fc1_size, fc2_size ) :
        super( QNetwork, self ).__init__()

        self.fc1 = nn.Linear( state_size, fc1_size )
        self.fc2 = nn.Linear( fc1_size, fc2_size )
        self.fc3 = nn.Linear( fc2_size, action_size )

    def forward( self, s ) :
        # Outputs a vector with all Q-values
        # for all actions possible
        x = F.relu( self.fc1( s ) )
        x = F.relu( self.fc2( x ) )
        return self.fc3( x )