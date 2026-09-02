document.addEventListener('DOMContentLoaded', () => {
    const howItWorksBtn = document.getElementById('how-it-works-btn');
    const videoModal = document.getElementById('video-modal');
    const closeModalBtn = document.getElementById('close-modal');
    const modalVideo = document.getElementById('modal-video');

    const videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1';

    if (howItWorksBtn && videoModal && closeModalBtn && modalVideo) {
        const openModal = (e) => {
            e.preventDefault();
            modalVideo.src = videoUrl;
            videoModal.style.display = 'flex';
            document.body.style.overflow = 'hidden'; // Prevent scrolling
        };

        const closeModal = () => {
            videoModal.style.display = 'none';
            modalVideo.src = ''; // Stop video playback
            document.body.style.overflow = ''; // Restore scrolling
        };

        howItWorksBtn.addEventListener('click', openModal);
        closeModalBtn.addEventListener('click', closeModal);

        // Close when clicking outside the modal content
        videoModal.addEventListener('click', (e) => {
            if (e.target === videoModal) {
                closeModal();
            }
        });
    }
});
