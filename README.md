# Evaluation Framework for Pseudoknotted RNA using Automatic Taxonomy Construction

The code and the data available in this project are a support for the paper "Evaluating Comparison Methods for Pseudoknotted RNAs through Automatic Taxonomy Construction" by Michela Quadrini, Luca Tesei, and Emanuela Merelli.

## Content

This project contains a Python script to process the data and the data themselves, as CSV files, in folder "Data".

## Requirements for running the script

* Python 3
* Scikit-learn 

## Use of the script

To obtain the clusterization of the paper, use the following command: 

`> python3 cluster.py —domain $X —method $Y`


You can select:
* the domain $X among “Archaea”, “Bacteria” or “Eukaryota”
* the method $Y to determine the distance among molecules among “Aspralign”, “Genus” or “Psmalign”

## Example of Runs with clustering linkage method "complete"

The command:

`> python Cluster.py --domain Archaea --method Aspralign`

clusterizes the molecules of Archaea by considering the distances computed via ASPRAlign

The obtained results is: 

```
	Domain: Archaea
	Method: Aspralign
	Rand_score 0.74
	Homogeneity_score 0.8377580405318166
	completeness_score 0.5640494394923921
```

The command:

`> python Cluster.py --domain Archaea --method Psmalign`

clusterizes the molecules of Archaea by considering the distances computed via Psmalign

The obtained results is 

```
	Domain: Archaea
	Method: Psmalign
	Rand_score 0.74
	Homogeneity_score 0.8377580405318166
	completeness_score 0.5640494394923921
```

The command:

`> python Cluster.py --domain Archaea --method Genus`

clusterizes the molecules of Archaea by considering the distances computed via Genus

The obtained results is 

```
	Domain: Archaea
	Method: Genus
	Rand_score 0.6033333333333334
	Homogeneity_score 0.25394481282729686
	completeness_score 0.5377833106096092
```

The command:

`> python3 cluster.py --domain Bacteria --method Aspralign`

clusterizes the molecules of Bacteria by considering the distances computed via ASPRAlign

The obtained results is 

```
	Domain: Bacteria
	Method: Aspralign
	Rand_score 0.8300029324284697
	Homogeneity_score 0.6754429441384708
	completeness_score 0.6085114022488246
```

The command:

`> python3 cluster.py --domain Bacteria --method Psmalign`

clusterizes the molecules of Bacteria by considering the distances computed via Psmalign

The obtained results is 

```
	Domain: Bacteria
	Method: Psmalign
	Rand_score 0.8630974823006996
	Homogeneity_score 0.8092402136009486
	completeness_score 0.6509952516123563
```

The command:

`> python3 cluster.py --domain Bacteria --method Genus`

clusterizes the molecules of Bacteria by considering the distances computed via Genus

The obtained results is 

```
	Domain: Bacteria
	Method: Genus
	Rand_score 0.4826777261111809
	Homogeneity_score 0.13711251019572268
	completeness_score 0.24206965147185627
```

The command:

`> python3 cluster.py --domain Eukaryota --method Aspralign`

clusterizes the molecules of Eukaryota by considering the distances computed via Aspralign

The obtained results is 

```
	Domain: Eukaryota
	Method: Aspralign
	Rand_score 0.7105575905575906
	Homogeneity_score 0.3316008110639983
	completeness_score 0.38370318340105897
```

The command:

`> python3 cluster.py —domain Eukaryota —method Psmalign`

clusterizes the molecules of Eukaryota by considering the distances computed via Psmalign

The obtained results is 

```
	Domain: Eukaryota
	Method: Psmalign
	Rand_score 0.7842246642246642
	Homogeneity_score 0.47175326752598523
	completeness_score 0.4448523228471222
```

The command:

`> python3 cluster.py —domain Eukaryota —method Genus`

clusterizes the molecules of Eukaryota by considering the distances computed via Genus

The obtained results is 

```
	Domain: Eukaryota
	Method: Genus
	Rand_score 0.5643304843304844
	Homogeneity_score 0.0862960329639474
	completeness_score 0.1396146707140499
```

## Results obtained with clustering linkage method "average"

### Archaea

Rand score - genus 0.6033333333333334
Homogeneity score - genus 0.25394481282729686
completeness score - genus 0.5377833106096092

Rand score - psmalign 0.44
Homogeneity score - psmalign 0.18686035555698258
completeness score - psmalign 0.16392462103371275

Rand score - Aspralign 0.7633333333333333
Homogeneity score - Aspralign 0.8377580405318164
completeness score - Aspralign 0.5822631209822778

### Bacteria
Rand score - genus 0.4826777261111809
Homogeneity score - genus 0.13711251019572268
completeness score - genus 0.24206965147185627

Rand score - psmalign 0.7538854677223409
Homogeneity score - psmalign 0.5931520859786583
completeness score - psmalign 0.7229374332921712

Rand score - Aspralign 0.8306732017929706
Homogeneity score - Aspralign 0.6428067678703644
completeness score - Aspralign 0.6246301072108581


### Eucaryota
Rand score - genus 0.5643304843304844
Homogeneity score - genus 0.0862960329639474
completeness score - genus 0.1396146707140499

Rand score - psmalign 0.4757834757834758
Homogeneity score - psmalign 0.20006721321034357
completeness score - psmalign 0.43477608977207155

Rand score - Aspralign 0.7153601953601954
Homogeneity score - Aspralign 0.3410525142148621
completeness score - Aspralign 0.41358734560471744


## Results obtained with clustering linkage method "single"

### Archaea
Rand score - genus 0.6033333333333334
Homogeneity score - genus 0.25394481282729686
completeness score - genus 0.5377833106096092

Rand score - psmalign 0.5733333333333334
Homogeneity score - psmalign 0.27147699058079666
completeness score - psmalign 0.4334416469662887

Rand score - Aspralign 0.9233333333333333
Homogeneity score - Aspralign 0.837758040531817
completeness score - Aspralign 0.7933166043659426

### Bacteria
Rand score - genus 0.4695236898328516
Homogeneity score - genus 0.13549830549968492
completeness score - genus 0.2554641777142576

Rand score - psmalign 0.5087763394914331
Homogeneity score - psmalign 0.38182667088112604
completeness score - psmalign 0.871848154045219

Rand score - Aspralign 0.4345858992082443
Homogeneity score - Aspralign 0.24445617730687746
completeness score - Aspralign 0.5607127650924485

### Eucaryota
Rand score - genus 0.5585022385022385
Homogeneity score - genus 0.07758106267715133
completeness score - genus 0.13103124195996946

Rand score - psmalign 0.2933007733007733
Homogeneity score - psmalign 0.08057066582191781
completeness score - psmalign 0.4541402778474564

Rand score - Aspralign 0.4548962148962149
Homogeneity score - Aspralign 0.18634078222112238
completeness score - Aspralign 0.4415328069074054

## Contact Information

Please report any issue to michela.quadrini@unicam.it or to Michela Quadrini, Polo
Informatico, via Madonna delle Carceri 9, 62032 Camerino (MC) Italy.


