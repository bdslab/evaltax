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

## Runs

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

## Contact Information

Please report any issue to michela.quadrini@unicam.it or to Michela Quadrini, Polo
Informatico, via Madonna delle Carceri 9, 62032 Camerino (MC) Italy.


