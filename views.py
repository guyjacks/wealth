from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class FieldWeight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hgnc_gene_gene_family(db.Integer)
    hgnc_locus_type(db.Integer)


"""
field definitions: http://www.genenames.org/help/symbol-report


"""
class HgncGene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hgnc_id = db.Column(db.String(20))
    symbol = db.Column(db.String(10))
    name = db.Column(db.String(80))
    # does not always exist
    gene_family = db.Column(db.String(80))
    locus_type = db.Column(db.String(80))


"""
A gene related to a second gene by descent from a common ancestral DNA sequence.
The term, homolog, may apply to the relationship between genes separated by the
event of speciation (see ortholog) or to the relationship betwen genes separated
by the event of genetic duplication (see paralog).
"""
class Homolog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

"""
Orthologs are genes in different species that evolved from a common ancestral
gene by speciation. Normally, orthologs retain the same function in the course
of evolution. Identification of orthologs is critical for reliable prediction of
gene function in newly sequenced genomes.

@source: Sources exist for each ortholog (i.e. MSI for mouse)

"""
class Ortholog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(20))
    # i.e. MGI, Ensembl, RGD, ...
    source = db.Column(db.String(20))
    source_id = db.Column(db.String(25)


"""
http://www.genenames.org/help/symbol-report#Locus_type

"""
class LocusType(db.Model):
    id = db.Column(db.Integer, primary_key=True)


"""
http://www.sequenceontology.org/browser/current_svn/term/SO:0001217

"""
class SequenceOntologyEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accession = db.Column(db.String(20))


"""


"""
class HgncGene_LocusType(db.Model):
    id = db.Column(db.Integer, primary_key=True)


"""
Locus types can have multiple subtypes

"""
class LocusType_SequenceOntologyEntity(db.Model):
