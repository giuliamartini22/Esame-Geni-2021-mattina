from database.DB_connect import DBConnect
from model.gene import Genes


class DAO():

    @staticmethod
    def get_all_chromosomes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct g.Chromosome as chr
                        from genes g 
                        where g.Chromosome > 0
                        """
            cursor.execute(query)

            for row in cursor:
                result.append(row["chr"])

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_edges():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select g1.Chromosome as c1, g2.Chromosome as c2, i.GeneID1 as g1, i.GeneID2 as g2, i.Expression_Corr as peso
                        from interactions i, genes g1, genes g2
                        where i.GeneID1 = g1.GeneID
                        and i.GeneID2 = g2.GeneID 
                        and g1.Chromosome <> g2.Chromosome
                        and g1.Chromosome > 0
                        and g2.Chromosome > 0
                        group by i.GeneID1, i.GeneID2"""
            cursor.execute(query)

            for row in cursor:
                result.append((row["c1"], row["c2"], row["g1"], row["g2"], row["peso"]))

            cursor.close()
            cnx.close()
        return result
