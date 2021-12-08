data {
    int<lower=0> I;         // number of solutes
    int<lower=0> J;         // number of solvents
    int<lower=0> K;         // number of latent dimensions
    real ln_gamma[I,J];     // matrix of logarithmic activity coefficient
    real<lower=0> sigma_0;  // prior standard deviation
    real<lower=0> lambda;   // likelihood scale
}

parameters {
    vector[K] u[I]; // solute feature vectors
    vector[K] v[J]; // solvent feature vectors
}

model {
    // draw feature vectors for all solutes and solvents
    for (i in 1:I)
        u[i] ~ normal(0,sigma_0);
    for (j in 1:J)
        v[j] ~ normal(0,sigma_0);
    
    // likelihood: model the probabilty of ln_gamma as a Cauchy distribution
    // around the dot product of the feature vectors
    for (i in 1:I) {
        for (j in 1:J) {
            if (ln_gamma[i,j] != 0) {
                ln_gamma[i,j] ~ cauchy(u[i]' * v[j],lambda);
            }
        }
    }
}