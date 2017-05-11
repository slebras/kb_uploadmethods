# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_uploadmethods(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def upload_fastq_file(self, params, context=None):
        """
        :param params: instance of type "UploadMethodParams"
           (sequencing_tech: sequencing technology name: output reads file
           name workspace_name: workspace name/ID of the object For files in
           user's staging area: fwd_staging_file_name: single-end fastq file
           name or forward/left paired-end fastq file name from user's
           staging area rev_staging_file_name: reverse/right paired-end fastq
           file name user's staging area For files from web: download_type:
           download type for web source fastq file ('Direct Download', 'FTP',
           'DropBox', 'Google Drive') fwd_file_url: single-end fastq file URL
           or forward/left paired-end fastq file URL rev_file_url:
           reverse/right paired-end fastq file URL urls_to_add: used for
           parameter-groups. dict of {fwd_file_url, rev_file_url, name,
           single_genome, interleaved, insert_size_mean and
           read_orientation_outward} Optional Params: single_genome: whether
           the reads are from a single genome or a metagenome. interleaved:
           whether reads is interleaved insert_size_mean: mean (average)
           insert length insert_size_std_dev: standard deviation of insert
           lengths read_orientation_outward: whether reads in a pair point
           outward) -> structure: parameter "workspace_name" of type
           "workspace_name" (workspace name of the object), parameter
           "fwd_staging_file_name" of type "fwd_staging_file_name" (input and
           output file path/url), parameter "rev_staging_file_name" of type
           "rev_staging_file_name", parameter "download_type" of type
           "download_type", parameter "fwd_file_url" of type "fwd_file_url",
           parameter "rev_file_url" of type "rev_file_url", parameter
           "sequencing_tech" of type "sequencing_tech", parameter "name" of
           type "name", parameter "urls_to_add" of type "urls_to_add" ->
           structure: parameter "fwd_file_url" of type "fwd_file_url",
           parameter "rev_file_url" of type "rev_file_url", parameter "name"
           of type "name", parameter "single_genome" of type "single_genome",
           parameter "interleaved" of type "interleaved", parameter
           "insert_size_mean" of type "insert_size_mean", parameter
           "insert_size_std_dev" of type "insert_size_std_dev", parameter
           "read_orientation_outward" of type "read_orientation_outward",
           parameter "single_genome" of type "single_genome", parameter
           "interleaved" of type "interleaved", parameter "insert_size_mean"
           of type "insert_size_mean", parameter "insert_size_std_dev" of
           type "insert_size_std_dev", parameter "read_orientation_outward"
           of type "read_orientation_outward"
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.upload_fastq_file',
            [params], self._service_ver, context)

    def upload_fasta_gff_file(self, params, context=None):
        """
        :param params: instance of type "UploadFastaGFFMethodParams"
           (Required: genome_name: output genome object name workspace_name:
           workspace name/ID of the object For staging area: fasta_file:
           fasta file containing assembled contigs/chromosomes gff_file: gff
           file containing predicted gene models and corresponding features
           Optional params: scientific_name: proper name for species, key for
           taxonomy lookup. Default to 'unknown_taxon' source: Source Of The
           GenBank File. Default to 'User' taxon_wsname - where the reference
           taxons are. Default to 'ReferenceTaxons' taxon_reference - if
           defined, will try to link the Genome to the specified taxonomy
           object release: Release Or Version Of The Source Data
           genetic_code: Genetic Code For The Organism type: 'Reference',
           'User upload', 'Representative') -> structure: parameter
           "fasta_file" of String, parameter "gff_file" of String, parameter
           "genome_name" of String, parameter "workspace_name" of type
           "workspace_name" (workspace name of the object), parameter
           "scientific_name" of String, parameter "source" of String,
           parameter "taxon_wsname" of String, parameter "taxon_reference" of
           String, parameter "release" of String, parameter "genetic_code" of
           Long, parameter "type" of String
        :returns: instance of type "UploadFastaGFFMethodResult" -> structure:
           parameter "genome_ref" of String, parameter "genome_info" of
           String, parameter "report_name" of type "report_name", parameter
           "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.upload_fasta_gff_file',
            [params], self._service_ver, context)

    def unpack_staging_file(self, params, context=None):
        """
        Unpack a staging area file
        :param params: instance of type "UnpackStagingFileParams" (Input
           parameters for the "unpack_staging_file" function. Required
           parameters: staging_file_subdir_path: subdirectory file path e.g.
           for file: /data/bulk/user_name/file_name staging_file_subdir_path
           is file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           workspace_name: workspace name/ID of the object) -> structure:
           parameter "workspace_name" of type "workspace_name" (workspace
           name of the object), parameter "staging_file_subdir_path" of String
        :returns: instance of type "UnpackStagingFileOutput" (Results from
           the unpack_staging_file function. unpacked_file_path: unpacked
           file path(s) in staging area) -> structure: parameter
           "unpacked_file_path" of String
        """
        return self._client.call_method(
            'kb_uploadmethods.unpack_staging_file',
            [params], self._service_ver, context)

    def unpack_web_file(self, params, context=None):
        """
        Download and unpack a web file to staging area
        :param params: instance of type "UnpackWebFileParams" (Input
           parameters for the "unpack_web_file" function. Required
           parameters: workspace_name: workspace name/ID of the object
           file_url: file URL download_type: one of ['Direct Download',
           'FTP', 'DropBox', 'Google Drive'] Optional:
           urls_to_add_web_unpack: used for parameter-groups. dict of
           {file_url}) -> structure: parameter "workspace_name" of type
           "workspace_name" (workspace name of the object), parameter
           "file_url" of String, parameter "download_type" of String,
           parameter "urls_to_add_web_unpack" of type
           "urls_to_add_web_unpack" -> structure: parameter "file_url" of
           String
        :returns: instance of type "UnpackWebFileOutput" (Results from the
           unpack_web_file function. unpacked_file_path: unpacked file
           path(s) in staging area) -> structure: parameter
           "unpacked_file_path" of String
        """
        return self._client.call_method(
            'kb_uploadmethods.unpack_web_file',
            [params], self._service_ver, context)

    def import_genbank_from_staging(self, params, context=None):
        """
        :param params: instance of type "GenbankToGenomeParams"
           (import_genbank_from_staging: wrapper method for
           GenomeFileUtil.genbank_to_genome required params:
           staging_file_subdir_path - subdirectory file path e.g. for file:
           /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           genome_name - becomes the name of the object workspace_name - the
           name of the workspace it gets saved to. source - Source of the
           file typically something like RefSeq or Ensembl optional params:
           release - Release or version number of the data per example
           Ensembl has numbered releases of all their data: Release 31
           generate_ids_if_needed - If field used for feature id is not
           there, generate ids (default behavior is raising an exception)
           genetic_code - Genetic code of organism. Overwrites determined GC
           from taxon object type - Reference, Representative or User upload)
           -> structure: parameter "staging_file_subdir_path" of String,
           parameter "genome_name" of String, parameter "workspace_name" of
           String, parameter "source" of String, parameter "release" of
           String, parameter "genetic_code" of Long, parameter "type" of
           String, parameter "generate_ids_if_needed" of String, parameter
           "exclude_ontologies" of String
        :returns: instance of type "GenomeSaveResult" -> structure: parameter
           "genome_ref" of String
        """
        return self._client.call_method(
            'kb_uploadmethods.import_genbank_from_staging',
            [params], self._service_ver, context)

    def import_sra_from_staging(self, params, context=None):
        """
        :param params: instance of type "SRAToReadsParams" (required params:
           staging_file_subdir_path: subdirectory file path e.g. for file:
           /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           sequencing_tech: sequencing technology name: output reads file
           name workspace_name: workspace name/ID of the object Optional
           Params: single_genome: whether the reads are from a single genome
           or a metagenome. insert_size_mean: mean (average) insert length
           insert_size_std_dev: standard deviation of insert lengths
           read_orientation_outward: whether reads in a pair point outward)
           -> structure: parameter "staging_file_subdir_path" of String,
           parameter "sequencing_tech" of type "sequencing_tech", parameter
           "name" of type "name", parameter "workspace_name" of type
           "workspace_name" (workspace name of the object), parameter
           "single_genome" of type "single_genome", parameter
           "insert_size_mean" of type "insert_size_mean", parameter
           "insert_size_std_dev" of type "insert_size_std_dev", parameter
           "read_orientation_outward" of type "read_orientation_outward"
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_sra_from_staging',
            [params], self._service_ver, context)

    def import_sra_from_web(self, params, context=None):
        """
        :param params: instance of type "WebSRAToReadsParams" -> structure:
           parameter "download_type" of String, parameter "sra_urls_to_add"
           of type "sra_urls_to_add" (download_type: download type for web
           source fastq file ('Direct Download', 'FTP', 'DropBox', 'Google
           Drive') sra_urls_to_add: dict of SRA file URLs required params:
           file_url: SRA file URL sequencing_tech: sequencing technology
           name: output reads file name workspace_name: workspace name/ID of
           the object Optional Params: single_genome: whether the reads are
           from a single genome or a metagenome. insert_size_mean: mean
           (average) insert length insert_size_std_dev: standard deviation of
           insert lengths read_orientation_outward: whether reads in a pair
           point outward) -> structure: parameter "file_url" of String,
           parameter "sequencing_tech" of type "sequencing_tech", parameter
           "name" of type "name", parameter "workspace_name" of type
           "workspace_name" (workspace name of the object), parameter
           "single_genome" of type "single_genome", parameter
           "insert_size_mean" of type "insert_size_mean", parameter
           "insert_size_std_dev" of type "insert_size_std_dev", parameter
           "read_orientation_outward" of type "read_orientation_outward"
        :returns: instance of type "WebSRAToReadsResult" -> structure:
           parameter "obj_refs" of list of String, parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_sra_from_web',
            [params], self._service_ver, context)

    def import_fasta_as_assembly_from_staging(self, params, context=None):
        """
        :param params: instance of type "FastaToAssemblyParams" (required
           params: staging_file_subdir_path: subdirectory file path e.g. for
           file: /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           assembly_name: output Assembly file name workspace_name: workspace
           name/ID of the object) -> structure: parameter
           "staging_file_subdir_path" of String, parameter "assembly_name" of
           String, parameter "workspace_name" of type "workspace_name"
           (workspace name of the object)
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_fasta_as_assembly_from_staging',
            [params], self._service_ver, context)

    def import_tsv_as_media_from_staging(self, params, context=None):
        """
        :param params: instance of type "FileToMediaParams" (required params:
           staging_file_subdir_path: subdirectory file path e.g. for file:
           /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           media_name: output Media file name workspace_name: workspace
           name/ID of the object) -> structure: parameter
           "staging_file_subdir_path" of String, parameter "media_name" of
           String, parameter "workspace_name" of type "workspace_name"
           (workspace name of the object)
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_tsv_as_media_from_staging',
            [params], self._service_ver, context)

    def import_excel_as_media_from_staging(self, params, context=None):
        """
        :param params: instance of type "FileToMediaParams" (required params:
           staging_file_subdir_path: subdirectory file path e.g. for file:
           /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           media_name: output Media file name workspace_name: workspace
           name/ID of the object) -> structure: parameter
           "staging_file_subdir_path" of String, parameter "media_name" of
           String, parameter "workspace_name" of type "workspace_name"
           (workspace name of the object)
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_excel_as_media_from_staging',
            [params], self._service_ver, context)

    def import_tsv_or_excel_as_media_from_staging(self, params, context=None):
        """
        :param params: instance of type "FileToMediaParams" (required params:
           staging_file_subdir_path: subdirectory file path e.g. for file:
           /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           media_name: output Media file name workspace_name: workspace
           name/ID of the object) -> structure: parameter
           "staging_file_subdir_path" of String, parameter "media_name" of
           String, parameter "workspace_name" of type "workspace_name"
           (workspace name of the object)
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_tsv_or_excel_as_media_from_staging',
            [params], self._service_ver, context)

    def import_tsv_as_expression_matrix_from_staging(self, params, context=None):
        """
        :param params: instance of type "FileToMatrixParams" (required
           params: staging_file_subdir_path: subdirectory file path e.g. for
           file: /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name
           matrix_name: output Expressin Matirx file name workspace_name:
           workspace name/ID of the object genome_ref: optional reference to
           a Genome object that will be used for mapping feature IDs to
           fill_missing_values: optional flag for filling in missing values
           in matrix (default value is false) data_type: optional filed,
           value is one of 'untransformed', 'log2_level', 'log10_level',
           'log2_ratio', 'log10_ratio' or 'unknown' (last one is default
           value) data_scale: optional parameter (default value is '1.0')) ->
           structure: parameter "staging_file_subdir_path" of String,
           parameter "workspace_name" of type "workspace_name" (workspace
           name of the object), parameter "matrix_name" of String, parameter
           "genome_ref" of String, parameter "fill_missing_values" of type
           "boolean" (Indicates true or false values, false = 0, true = 1
           @range [0,1]), parameter "data_type" of String, parameter
           "data_scale" of String
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_tsv_as_expression_matrix_from_staging',
            [params], self._service_ver, context)

    def import_reads_from_staging(self, params, context=None):
        """
        :param params: instance of type "UploadReadsParams" (sequencing_tech:
           sequencing technology name: output reads file name workspace_name:
           workspace name/ID of the object import_type: either FASTQ or SRA
           For files in user's staging area:
           fastq_fwd_or_sra_staging_file_name: single-end fastq file name Or
           forward/left paired-end fastq file name from user's staging area
           Or SRA staging file fastq_rev_staging_file_name: reverse/right
           paired-end fastq file name user's staging area e.g. for file:
           /data/bulk/user_name/file_name staging_file_subdir_path is
           file_name for file:
           /data/bulk/user_name/subdir_1/subdir_2/file_name
           staging_file_subdir_path is subdir_1/subdir_2/file_name Optional
           Params: single_genome: whether the reads are from a single genome
           or a metagenome. interleaved: whether reads is interleaved
           insert_size_mean: mean (average) insert length
           insert_size_std_dev: standard deviation of insert lengths
           read_orientation_outward: whether reads in a pair point outward)
           -> structure: parameter "import_type" of String, parameter
           "fastq_fwd_staging_file_name" of String, parameter
           "fastq_rev_staging_file_name" of String, parameter
           "sra_staging_file_name" of String, parameter "sequencing_tech" of
           type "sequencing_tech", parameter "workspace_name" of type
           "workspace_name" (workspace name of the object), parameter "name"
           of String, parameter "single_genome" of type "single_genome",
           parameter "interleaved" of type "interleaved", parameter
           "insert_size_mean" of type "insert_size_mean", parameter
           "insert_size_std_dev" of type "insert_size_std_dev", parameter
           "read_orientation_outward" of type "read_orientation_outward"
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref", parameter "report_name" of
           type "report_name", parameter "report_ref" of type "report_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.import_reads_from_staging',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_uploadmethods.status',
                                        [], self._service_ver, context)
