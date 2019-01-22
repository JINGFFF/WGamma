import json

xs_inputs_muon = json.load(open("xs_inputs/xs_inputs_muon.txt"))
xs_inputs_electron = json.load(open("xs_inputs/xs_inputs_electron.txt"))

from pprint import pprint

pprint(xs_inputs_muon)
pprint(xs_inputs_electron)

assert(xs_inputs_muon["fiducial_region_cuts_efficiency"] == xs_inputs_electron["fiducial_region_cuts_efficiency"])
assert(xs_inputs_muon["n_weighted_run_over"] == xs_inputs_electron["n_weighted_run_over"])

fiducial_region_cuts_efficiency  =  xs_inputs_muon["fiducial_region_cuts_efficiency"]
n_weighted_run_over  =  xs_inputs_muon["n_weighted_run_over"]

n_signal_muon  =  xs_inputs_muon["n_signal_muon"]
n_signal_syst_unc_due_to_fake_photon_muon  =  xs_inputs_muon["n_signal_syst_unc_due_to_fake_photon_muon"]
n_signal_syst_unc_due_to_fake_lepton_muon  =  xs_inputs_muon["n_signal_syst_unc_due_to_fake_lepton_muon"]
n_signal_stat_unc_muon  =  xs_inputs_muon["n_signal_stat_unc_muon"]
n_weighted_selected_data_mc_sf_muon  =  xs_inputs_muon["n_weighted_selected_data_mc_sf_muon"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_id_sf_muon  =  xs_inputs_muon["n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_id_sf_muon"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_iso_sf_muon  =  xs_inputs_muon["n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_iso_sf_muon"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_muon  =  xs_inputs_muon["n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_muon"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_muon  =  xs_inputs_muon["n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_muon"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_muon  =  xs_inputs_muon["n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_muon"]

n_signal_electron  =  xs_inputs_electron["n_signal_electron"]
n_signal_syst_unc_due_to_fake_photon_electron  =  xs_inputs_electron["n_signal_syst_unc_due_to_fake_photon_electron"]
n_signal_syst_unc_due_to_fake_lepton_electron  =  xs_inputs_electron["n_signal_syst_unc_due_to_fake_lepton_electron"]
n_signal_stat_unc_electron  =  xs_inputs_electron["n_signal_stat_unc_electron"]
n_weighted_selected_data_mc_sf_electron  =  xs_inputs_electron["n_weighted_selected_data_mc_sf_electron"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_id_sf_electron  =  xs_inputs_electron["n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_id_sf_electron"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_reco_sf_electron  =  xs_inputs_electron["n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_reco_sf_electron"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_electron =   xs_inputs_electron["n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_electron"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_electron  =  xs_inputs_electron["n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_electron"]
n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_electron  =  xs_inputs_electron["n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_electron"]

import math

n_signal = n_signal_muon+n_signal_electron

n_signal_syst_unc_due_to_fake_photon = n_signal_syst_unc_due_to_fake_photon_electron+n_signal_syst_unc_due_to_fake_photon_muon

n_signal_syst_unc_due_to_fake_lepton = n_signal_syst_unc_due_to_fake_lepton_electron+n_signal_syst_unc_due_to_fake_lepton_muon

n_weighted_selected_data_mc_sf = n_weighted_selected_data_mc_sf_electron + n_weighted_selected_data_mc_sf_muon

n_signal_stat_unc = math.sqrt(pow(n_signal_stat_unc_electron,2) + pow(n_signal_stat_unc_muon,2))

n_weighted_selected_data_mc_sf_syst_unc = math.sqrt(pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_id_sf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_iso_sf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_id_sf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_reco_sf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_electron,2))

n_weighted_selected_data_mc_sf_syst_unc_muon = math.sqrt(pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_id_sf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_iso_sf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_muon,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_muon,2))

n_weighted_selected_data_mc_sf_syst_unc_electron = math.sqrt(pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_id_sf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_reco_sf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_electron,2)+pow(n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_electron,2))

xs =  n_signal/(n_weighted_selected_data_mc_sf*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency)

xs_electron =  n_signal_electron/(n_weighted_selected_data_mc_sf_electron*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency)

xs_muon =  n_signal_muon/(n_weighted_selected_data_mc_sf_muon*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency)

lumi_err =  n_signal/(n_weighted_selected_data_mc_sf*35.9*0.975*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

lumi_err_electron =  n_signal_electron/(n_weighted_selected_data_mc_sf_electron*35.9*0.975*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs_electron

lumi_err_muon =  n_signal_muon/(n_weighted_selected_data_mc_sf_muon*35.9*0.975*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs_muon

stat_err = (n_signal+n_signal_stat_unc)/(n_weighted_selected_data_mc_sf*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs_muon

stat_err_electron = (n_signal_electron+n_signal_stat_unc_electron)/(n_weighted_selected_data_mc_sf_electron*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs_electron

stat_err_muon = (n_signal_muon+n_signal_stat_unc_muon)/(n_weighted_selected_data_mc_sf_muon*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs_muon

syst_err_acc = n_signal/((n_weighted_selected_data_mc_sf - n_weighted_selected_data_mc_sf_syst_unc)*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_acc_muon = n_signal_muon/((n_weighted_selected_data_mc_sf_muon - n_weighted_selected_data_mc_sf_syst_unc_muon)*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_acc_electron = n_signal_electron/((n_weighted_selected_data_mc_sf_electron - n_weighted_selected_data_mc_sf_syst_unc_electron)*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_n_signal_fake_photon = (n_signal+n_signal_syst_unc_due_to_fake_photon)/(n_weighted_selected_data_mc_sf*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_n_signal_muon_fake_photon = (n_signal_muon+n_signal_syst_unc_due_to_fake_photon_muon)/(n_weighted_selected_data_mc_sf_muon*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_n_signal_electron_fake_photon = (n_signal_electron+n_signal_syst_unc_due_to_fake_photon_electron)/(n_weighted_selected_data_mc_sf_electron*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_n_signal_fake_lepton = (n_signal+n_signal_syst_unc_due_to_fake_lepton)/(n_weighted_selected_data_mc_sf*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_n_signal_muon_fake_lepton = (n_signal_muon+n_signal_syst_unc_due_to_fake_lepton_muon)/(n_weighted_selected_data_mc_sf_muon*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err_n_signal_electron_fake_lepton = (n_signal_electron+n_signal_syst_unc_due_to_fake_lepton_electron)/(n_weighted_selected_data_mc_sf_electron*35.9*1000/n_weighted_run_over/fiducial_region_cuts_efficiency) - xs

syst_err = math.sqrt(pow(syst_err_n_signal_fake_photon,2)+pow(syst_err_n_signal_fake_lepton,2)+pow(syst_err_acc,2))

syst_err_electron = math.sqrt(pow(syst_err_n_signal_electron_fake_photon,2)+pow(syst_err_n_signal_electron_fake_lepton,2)+pow(syst_err_acc_electron,2))

syst_err_muon = math.sqrt(pow(syst_err_n_signal_muon_fake_photon,2)+pow(syst_err_n_signal_muon_fake_lepton,2)+pow(syst_err_acc_muon,2))

acc = n_weighted_selected_data_mc_sf/n_weighted_run_over/fiducial_region_cuts_efficiency

acc_electron = n_weighted_selected_data_mc_sf_electron/n_weighted_run_over/fiducial_region_cuts_efficiency

acc_muon = n_weighted_selected_data_mc_sf_muon/n_weighted_run_over/fiducial_region_cuts_efficiency

fractional_err_on_acc_due_to_pdf = (((n_weighted_selected_data_mc_sf + n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_muon)/n_weighted_run_over) - acc)/acc

fractional_err_on_acc_due_to_pdf_electron = (((n_weighted_selected_data_mc_sf_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_electron)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_electron)/acc_electron

fractional_err_on_acc_due_to_pdf_muon = (((n_weighted_selected_data_mc_sf_muon + n_weighted_selected_data_mc_sf_syst_unc_due_to_pdf_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_muon)/acc_muon

fractional_err_on_acc_due_to_qcd_scale = (((n_weighted_selected_data_mc_sf + n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc)/acc

fractional_err_on_acc_due_to_qcd_scale_electron = (((n_weighted_selected_data_mc_sf_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_electron)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_electron)/acc_electron

fractional_err_on_acc_due_to_qcd_scale_muon = (((n_weighted_selected_data_mc_sf_muon + n_weighted_selected_data_mc_sf_syst_unc_due_to_qcd_scale_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_muon)/acc_muon

fractional_err_on_acc_due_to_photon_id_sf = (((n_weighted_selected_data_mc_sf + n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc)/acc

fractional_err_on_acc_due_to_photon_id_sf_electron = (((n_weighted_selected_data_mc_sf_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_electron)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_electron)/acc_electron

fractional_err_on_acc_due_to_photon_id_sf_muon = (((n_weighted_selected_data_mc_sf_muon +n_weighted_selected_data_mc_sf_syst_unc_due_to_photon_id_sf_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_muon)/acc_muon

fractional_err_on_acc_due_to_electron_reco_sf = (((n_weighted_selected_data_mc_sf + n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_reco_sf_electron)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc)/acc

fractional_err_on_acc_due_to_electron_reco_sf_electron = (((n_weighted_selected_data_mc_sf_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_reco_sf_electron)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_electron)/acc_electron

fractional_err_on_acc_due_to_electron_id_sf = (((n_weighted_selected_data_mc_sf + n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_id_sf_electron)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc)/acc

fractional_err_on_acc_due_to_electron_id_sf_electron = (((n_weighted_selected_data_mc_sf_electron + n_weighted_selected_data_mc_sf_syst_unc_due_to_electron_id_sf_electron)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_electron)/acc_electron

fractional_err_on_acc_due_to_muon_id_sf = (((n_weighted_selected_data_mc_sf + n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_id_sf_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc)/acc

fractional_err_on_acc_due_to_muon_id_sf_muon = (((n_weighted_selected_data_mc_sf_muon + n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_id_sf_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_muon)/acc_muon

fractional_err_on_acc_due_to_muon_iso_sf = (((n_weighted_selected_data_mc_sf + n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_iso_sf_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc)/acc

fractional_err_on_acc_due_to_muon_iso_sf_muon = (((n_weighted_selected_data_mc_sf_muon + n_weighted_selected_data_mc_sf_syst_unc_due_to_muon_iso_sf_muon)/n_weighted_run_over/fiducial_region_cuts_efficiency) - acc_muon)/acc_muon

print "xs = " +str(xs) + " +/- " + str(stat_err) + " (stat) +/- " + str(syst_err) + " (syst) +/- " + str(lumi_err) + " (lumi)"

print "xs based on electron channel = " +str(xs_electron) + " +/- " + str(stat_err_electron) + " (stat) +/- " + str(syst_err_electron) + " (syst) +/- "  + str(lumi_err_electron) + " (lumi)"

print "xs based on muon channel = " +str(xs_muon) + " +/- "+ str(stat_err_muon) + " (stat) +/- " + str(syst_err_muon) + " (syst) +/- "  + str(lumi_err_muon) + " (lumi)" 

print "syst_err_n_signal_fake_photon = "+str(syst_err_n_signal_fake_photon)

print "syst_err_n_signal_electron_fake_photon = "+str(syst_err_n_signal_electron_fake_photon)

print "syst_err_n_signal_muon_fake_photon = "+str(syst_err_n_signal_muon_fake_photon)

print "acc = "+str(acc)

print "acc_muon = "+str(acc_muon)

print "acc_electron = "+str(acc_electron)

print "fractional_err_on_acc_due_to_pdf = " + str(fractional_err_on_acc_due_to_pdf)

print "fractional_err_on_acc_due_to_pdf_muon = " + str(fractional_err_on_acc_due_to_pdf_muon)

print "fractional_err_on_acc_due_to_pdf_electron = " + str(fractional_err_on_acc_due_to_pdf_electron)

print "fractional_err_on_acc_due_to_qcd_scale = " + str(fractional_err_on_acc_due_to_qcd_scale)

print "fractional_err_on_acc_due_to_qcd_scale_electron = " + str(fractional_err_on_acc_due_to_qcd_scale_electron)

print "fractional_err_on_acc_due_to_qcd_scale_muon = " + str(fractional_err_on_acc_due_to_qcd_scale_muon)

print "fractional_err_on_acc_due_to_photon_id_sf = "+ str(fractional_err_on_acc_due_to_photon_id_sf)

print "fractional_err_on_acc_due_to_photon_id_sf_electron = "+ str(fractional_err_on_acc_due_to_photon_id_sf_electron)

print "fractional_err_on_acc_due_to_photon_id_sf_muon = "+ str(fractional_err_on_acc_due_to_photon_id_sf_muon)

print "fractional_err_on_acc_due_to_electron_reco_sf = " + str(fractional_err_on_acc_due_to_electron_reco_sf)

print "fractional_err_on_acc_due_to_electron_reco_sf_electron = " + str(fractional_err_on_acc_due_to_electron_reco_sf_electron)

print "fractional_err_on_acc_due_to_electron_id_sf = " + str(fractional_err_on_acc_due_to_electron_id_sf)

print "fractional_err_on_acc_due_to_electron_id_sf_electron = " + str(fractional_err_on_acc_due_to_electron_id_sf_electron)

print "fractional_err_on_acc_due_to_muon_id_sf = " + str(fractional_err_on_acc_due_to_muon_id_sf)

print "fractional_err_on_acc_due_to_muon_id_sf_muon = " + str(fractional_err_on_acc_due_to_muon_id_sf_muon)

print "fractional_err_on_acc_due_to_muon_iso_sf = " + str(fractional_err_on_acc_due_to_muon_iso_sf)

print "fractional_err_on_acc_due_to_muon_iso_sf_muon = " + str(fractional_err_on_acc_due_to_muon_iso_sf_muon)
