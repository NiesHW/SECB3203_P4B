# CLASSIFICATION of malaria disease (MalariaDetect)

# Member Name:
- Muhammad Saifuddin A21EC0093
- Adam Afiq B22EC0012

Project Progress:
12/10/2023 - Make an appointment with sir hairuddin to discuss about Malaria disease 

Reference : 
1. https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=malaysia+data+for+malaria&btnG=#d=gs_qabs&t=1697082320216&u=%23p%3DDsC5HWbYPkoJ
2. https://malariajournal.biomedcentral.com/articles/10.1186/s12936-020-3135-x
3. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6603864/ (research about malaria)
4. https://www.mdpi.com/1424-8220/23/3/1501# (deep learning method)
method)
# MalariaDetect: A Machine Learning Model for Malaria Diagnosis

## 1.0 Introduction

Malaria is a dangerous infectious disease caused by Plasmodium parasites, which are transmitted to humans by the bite of an infected mosquito. It is common in many parts of the world, particularly in tropical and subtropical regions like Malaysia. In Malaysia, 16,500 malaria cases were reported between 2013 and 2017 (Narwani, 2020). These cases vary from mild malaria which resembles the flu to severe malaria which can cause brain infection. Malaria symptoms include high fevers and chills, as well as lethargy, headaches, and muscle aches. The parasite infects your red blood cells, causing you to become weak and ill. It also can lead to life-threatening complications in certain severe situations.

Plasmodium falciparum is the most severe and life-threatening kind of malaria and is responsible for the vast majority of malaria-related deaths; it is most commonly seen in Africa. Plasmodium vivax, which is widespread in the Middle East, and Central and South America, can cause relapses of the disease but is less lethal than Plasmodium falciparum. Plasmodium ovale is similar to Plasmodium vivax in that it can produce relapses. It is a less frequent kind of malaria that is found primarily in Africa and the Pacific. Then, there's Plasmodium malariae, which causes milder and less severe symptoms and is present in tropical and subtropical parts of Central and South America, Africa, and Southeast Asia (Toshi, 2023).

Malaria can be detected using the blood smear method. The method is where the doctor will examine a blood smear under a microscope. First, a sample is collected. Then, create a thin and even layer on the glass slide, we will examine the blood smear for the presence of malaria parasites, which can often be observed in various stages within red blood cells, depending on the Plasmodium species responsible for the infection. The procedure enables direct identification of the parasites, confirming malaria diagnosis and identifying the Plasmodium species (Healthwise, 2023). This method is especially useful in detecting malaria but it still has its limitations. That is why we propose MalariaDetect, a program where we will use deep learning technologies such as Convolutional Neural Networks (CNNs) to detect malaria by using the dataset of previous malaria patients so that our program will learn the pattern between all the datasets. This will allow our program, MalariaDetect to revolutionize the malaria detection method and save so many lives from this terrible disease.

## 1.1 Problem Background

Malaria is a dangerous disease caused by parasites transmitted to humans through the bites of infected mosquitoes. This disease is endemic in many parts of the world and it is estimated that more than 200 million people are infected each year. Early detection and treatment of malaria is essential to reduce morbidity and mortality, especially in developing countries where the disease is most common.

Microscopic examination of blood stains is the gold standard for diagnosing malaria. However, this method is time-consuming and requires trained personnel. Additionally, the accuracy of microscopic diagnosis can be influenced by a number of factors, including the quality of the blood smear, the experience of the microscopist, and parasite density in the blood.

## 1.2 Problem Statement

The malaria problem is about developing new diagnostic tools and strategies that are accurate, affordable, and accessible as well as enhancing the capacity of health systems to effectively diagnose and treat malaria.

MalariaDetect is a machine learning model developed to address the challenges of malaria diagnosis. MalariaDetect is trained on a large dataset of blood samples from patients with and without malaria. This model can determine with high accuracy the presence of malaria parasites in blood samples. MalariaDetect has the potential to revolutionize the way malaria is diagnosed and treated and could help improve the lives of millions of people around the world.

## 1.3 Objectives

The goal of MalariaDetect is to develop a machine-learning model that can accurately and effectively detect the presence of malaria parasites in blood samples. MalariaDetect has the potential to revolutionize the way malaria is diagnosed and treated and could help improve the lives of millions of people around the world.

MalariaDetect can be used to improve the accuracy of malaria diagnosis in several ways. First, MalariaDetect can be used to assist microscopists in making diagnoses. Second, MalariaDetect can be used to diagnose malaria in cases where microscopic diagnosis is not feasible, such as in remote areas or areas with high malaria prevalence. Third, MalariaDetect can be used to develop new diagnostic tools, such as point-of-care devices that can be used to diagnose malaria in the field.

MalariaDetect has the potential to improve the lives of millions of people around the world by making malaria diagnosis more accurate, more effective, and more accessible. This could lead to earlier diagnosis and treatment of malaria, which in turn could reduce morbidity and mortality. Additionally, MalariaDetect may help reduce the overuse of antimalarial drugs, which may contribute to the development of drug resistance.

Overall, MalariaDetect's goal is to help reduce the burden of malaria worldwide and improve the health and well-being of people living in malaria-endemic areas.

## 1.4 Scopes

The scope of our research project "MalariaDetect: A Machine Learning Model for Malaria Diagnosis" is centered around using deep learning such as Convolutional Neural Networks (CNNs) for the accurate and efficient identification of malaria parasites in blood smear images. Our scope encompasses several considerations:
- In terms of data, the project will use the publicly available dataset from an internet research journal about malaria incidents in Malaysia from 2013 to 2017. These datasets will span various types such as gender, age, race, state, infection kind, parasite type, and outcome of the patient.
- The research's domain of investigation revolves around using deep learning methods for malaria diagnosis. Our assumption is it will generate a much more accurate and precise result compared to the current method. Techniques that can be used is CNNs where blood smear images of previous patients of malaria will be used to establish a pattern on how to detect malaria. While our current target is the malaria cases in Malaysia, this research is not limited to that region, making it applicable to malaria diagnosis in diverse regions.
- The methodology employed involves the development and evaluation of deep learning models using deep frameworks.Model testing and validation will be conducted on separate datasets to create a performance measurement. This research sets the boundaries of its focus by specifying similarities between samples of patients that have malaria by utilizing historical trend analysis and thus creating a program that can separate between malaria-infected and non-infected.

## 1.5 Conclusion

The goal of our research project, "MalariaDetect: A Machine Learning Model for Malaria Diagnosis," is to use machine learning to combat malaria, one of the deadliest diseases in the world. Using a combination of deep learning approaches, our goal was to create a model that could diagnose malaria effectively and efficiently. To contribute to the body of medical knowledge that is already in existence, we want to enhance the early detection of this potentially fatal disease as we set out to reinvent the way malaria is identified with this project.
The accurate detection of malaria parasites was our primary objective as we designed and implemented a machine-learning model. Through extensive research, we discovered that CNNs can be an effective diagnostic tool for malaria, identifying contaminated blood samples with a high degree of accuracy. However, we also found that other deep learning approaches, such as recurrent neural networks (RNNs) and long short-term memory (LSTM) can also be used. Our study contributes to the existing method by showcasing the potential of machine learning, especially deep learning, in the field of malaria diagnosis.

In conclusion, "MalariaDetect: A Machine Learning Model for Malaria Diagnosis" marks the beginning of a journey for us to improve malaria diagnosis, which can ultimately lead to timely treatment and better health outcomes. With our commitment to further research and innovation, we are optimistic about the impact of our research, that is how deep learning can be used to diagnose malaria someday can be an achievement in the medical field. Furthermore, maybe in the future, our research on the use of machine learning models will not be limited to the diagnosis of malaria and also can be used to diagnose other diseases such as cancer, leukemia, thalassemia, and more so that it will be beneficial to the medical societies.
